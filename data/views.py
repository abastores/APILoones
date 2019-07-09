from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import Category, DataPrice, SubCategory
from .serializers import UserSerializer, GroupSerializer, CategorySerializer, SubCategorySerializer, DataPriceSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class DataPriceViewSet(viewsets.ModelViewSet):
    queryset = DataPrice.objects.all()
    serializer_class = DataPriceSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer