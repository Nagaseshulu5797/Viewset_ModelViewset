from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.models import *
from app.serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
class ProductCrudModelViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=Productserializers