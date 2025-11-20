from . models import ProductList
from rest_framework import serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields  = '__all__'