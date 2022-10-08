from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products_view, name='products'),
    path('category/<str:cat_slug>/', category_view, name='category'),
    path('clients/', clients_view, name='clients'),
    path('orders/', orders_view, name='orders'),
    path('product/<slug:product_slug>/', show_product_name_view, name='product_name'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
