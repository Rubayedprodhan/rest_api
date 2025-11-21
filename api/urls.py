from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('products', views.ProductViewSet, basename="products")
router.register('reviews', views.ReviewViewSet, basename="reviews")

urlpatterns = [
    path('',include(router.urls))

#     path('',views.Productlist_createView.as_view()),
#     path('<pk>/',views.ProductDetatilView.as_view()),
#     path('reviews/',views.ReviewerListCreate.as_view()),
#     path('review/<pk>/',views.ReviewerDetailView.as_view(), name='review_list')
]
