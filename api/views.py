from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Annuity
from .serializers import AnnuitySerializer

# Create your views here.
class Annuities(APIView):
    def get(self, request):
        annuities = Annuity.objects.all()
        data = AnnuitySerializer(annuities, many=True).data
        return Response(data)

    def post(self, request):
        """Create Request"""
        annuity = AnnuitySerializer(data=request.data['annuity'])
        if annuity.is_valid():
            a = annuity.save()
            return Response(annuity.data, status=status.HTTP_201_CREATED)
        else:
            return Response(annuity.errors, status=status.HTTP_400_BAD_REQUEST)
