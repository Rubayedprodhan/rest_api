from django.shortcuts import render, get_object_or_404
from . import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
@api_view(['GET', 'POST'])

# def product_list(request):
#     product = models.ProductList.objects.all()
#     serializer = serializers.ProductSerializer(product, many=True)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
def product_list(request):
    if request.method =='GET':
        product = models.ProductList.objects.all()
        serializer = serializers.ProductSerializer (product, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
         serializer = serializers.ProductSerializer (data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH', 'DELETE']) 
def product_detail(request, pk):
    product = get_object_or_404(request, pk=pk)
    if request.method == 'GET':
        serializer = serializers.ProductSerializer(product, status= status.HTTP_200_OK)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':

        serializer = serializers.ProductSerializer(request, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method== 'PATCH':
        serializer = serializers.ProductSerializer(request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message' : 'Movie deleted successfully'})
            
