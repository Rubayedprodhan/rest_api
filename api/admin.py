from django.contrib import admin
from . models import ProductList, Rewiews
# Register your models here.
@admin.register(ProductList)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active']




@admin.register(Rewiews)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ['product', 'reviewer', 'rating']