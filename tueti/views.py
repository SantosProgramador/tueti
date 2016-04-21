from django.shortcuts import render
from tueti.models import Tuet
from tueti.serializers import TuetSerializer

from rest_framework import generics


# Create your views here.
class TuetListAPI(generics.ListAPIView):
    queryset = Tuet.objects.all()
    serializer_class = TuetSerializer

