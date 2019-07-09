from django.contrib.auth.models import User, Group
from .models import Category, DataPrice
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'add_date', 'update_date')

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'add_date', 'update_date', 'category')


class DataPriceSerializer(serializers.ModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(read_only=True) 

    class Meta:
        model = DataPrice
        fields = ('id', 'price', 'date', 'add_date', 'subcategory')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')