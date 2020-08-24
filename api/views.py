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

class AnnuityDetail(APIView):
    def get(self, request, pk):
        """Show Request"""
        annuity = get_object_or_404(Annuity, pk=pk)
        data = AnnuitySerializer(annuity).data
        return Response(data)

    def delete(self, request, pk):
        """Delete Request"""
        annuity = get_object_or_404(Annuity, pk=pk)
        annuity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        """Update Request"""
        annuity = get_object_or_404(Annuity, pk=pk)
        annuity_serialized = AnnuitySerializer(annuity, data=request.data['annuity'])
        if annuity_serialized.is_valid():
            annuity_serialized.save()
            return Response(annuity_serialized.data)
        else:
            return Response(annuity_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
