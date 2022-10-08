from django.contrib import admin
from .models import *


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_id', 'client_number', 'client_address')
    search_fields = ('client_name', 'client_number',)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name', )}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category')
    prepopulated_fields = {'slug': ('product_name', 'category')}


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)

