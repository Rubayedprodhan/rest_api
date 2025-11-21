from django.shortcuts import render, get_object_or_404
from . import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from . import permissions
# def product_list(request):
#     product = models.ProductList.objects.all()
#     serializer = serializers.ProductSerializer(product, many=True)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
# def product_list(request):
#     if request.method =='GET':
#         product = models.ProductList.objects.all()
#         serializer = serializers.ProductSerializer (product, many= True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#          serializer = serializers.ProductSerializer (data = request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data, status=status.HTTP_200_OK)
#          return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET' 'PUT', 'PATCH', 'DELETE']) 
# def product_detail(request, pk):
#     product = get_object_or_404(request, pk=pk)
#     if request.method == 'GET':
#         serializer = serializers.ProductSerializer(product, status= status.HTTP_200_OK)
#         return Response(serializer.data, status = status.HTTP_200_OK)
#     elif request.method == 'PUT':

#         serializer = serializers.ProductSerializer(request, data=request.data)
#         return Response(serializer.data, status = status.HTTP_200_OK)
#     elif request.method== 'PATCH':
#         serializer = serializers.ProductSerializer(request, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response({'message' : 'Movie deleted successfully'})

# class Productlist_createView(generics.ListCreateAPIView):
#     queryset = models.ProductList.objects.all()
#     serializer_class = serializers.ProductSerializer

# class ProductDetatilView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.ProductList.objects.all()
#     serializer_class = serializers.ProductSerializer


# class ReviewerListCreate(generics.ListCreateAPIView):
#     queryset = models.Rewiews.objects.all()
#     serializer_class = serializers.ReviewerSerializer



# class ReviewerDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Rewiews.objects.all()
#     serializer_class = serializers.ReviewerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.ProductList.objects.prefetch_related('reviews')
    serializer_class = serializers.ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Rewiews.objects.select_related('product')
    serializer_class = serializers.ReviewerSerializer
    permission_classes = [permissions.IsreviewerOrReadOnly, IsAuthenticated]
