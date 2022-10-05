from django.contrib import admin
from .models import Products, Clients, Clientcarts, Cartmeta, Orders, OrderedGoods


admin.site.register([Products, Clients, Clientcarts, Cartmeta, Orders, OrderedGoods], )
# Register your models here.
