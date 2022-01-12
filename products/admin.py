from django.contrib import admin
from .models import Product

# admin.site.register(Product)
#Кастомизация админки
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'in_store']
	list_filter = ['category']
	search_fields = ['name']
