from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import *

from .forms import UserAuthentication, UserSignupForm


navbar = [{'title': 'Home', 'url_name': 'shop:index'},
          {'title': 'Products', 'url_name': 'shop:products'},
          {'title': 'Clients', 'url_name': 'shop:clients'},
          {'title': 'Orders', 'url_name': 'shop:orders'},
          {'title': 'Log in', 'url_name': 'shop:login'},
          ]


def index(request):
    products = Products.objects.all()

    context = {'title': 'Main',
               'navbar': navbar,
               'products': products,
               'cat_selected': 'all',
               }

    return render(request, 'shop/index.html', context=context)


def products_view(request):
    return HttpResponse("Products")


def clients_view(request):
    return HttpResponse("Clients")


def orders_view(request):
    return HttpResponse("Orders")


def category_view(request, cat_slug):
    products = Products.objects.filter(category=cat_slug)

    if len(products) == 0:
        raise Http404()

    context = {'title': 'Show by category',
               'navbar': navbar,
               'products': products,
               'cat_selected': cat_slug,
               }

    return render(request, 'shop/index.html', context=context)


def show_product_name_view(request, product_slug):
    prod = get_object_or_404(Products, slug=product_slug)

    context = {'title': prod.product_name,
               'navbar': navbar,
               'products': prod,
               'cat_selected': prod.category.name,
               }

    return render(request, 'shop/product.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = UserAuthentication(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:index')

    else:
        form = UserAuthentication()

    return render(request, 'shop/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:login')

    else:
        form = UserSignupForm()

    return render(request, 'shop/signup.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        print('a')
        logout(request)
        return redirect('shop:login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
