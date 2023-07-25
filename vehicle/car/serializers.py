from rest_framework import serializers
from .models import Cars, Brand
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Brand
        fields = ['name', 'launch', 'style']

class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Cars
        fields = ['name', 'price', 'fuel', 'seat']


         