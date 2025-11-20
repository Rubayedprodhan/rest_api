from django.contrib import admin
from . models import ProductList
# Register your models here.
@admin.register(ProductList)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active']