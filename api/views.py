from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Annuity

# Create your views here.
class Annuities(APIView):
    def get(self, request):
        annuities = Annuity.objects.all()
        return Response(annuities)
