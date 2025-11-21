from .models import ProductList, Rewiews
from rest_framework import serializers



class ReviewerSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()
    class Meta:
        model = Rewiews
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    reviews= ReviewerSerializer(many = True, read_only = True)
  
    #reviews= serializers.StringRelatedField(many = True, read_only = True)
    #reviews= serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    #reviews= serializers.HyperlinkedRelatedField(many=True, read_only=True)
    class Meta:
        model = ProductList
        fields  = '__all__'