from django.shortcuts import render
from .serializers import CarsSerializer, BrandSerializer
from rest_framework import viewsets
from .models import Brand, Cars

class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarsViewset(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer