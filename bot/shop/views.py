from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout

from .forms import UserAuthentication, UserSignupForm


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('shop:index')

    else:
        form = UserSignupForm()

    return render(request, 'shop/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserAuthentication(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'shop/index.html')

    else:
        form = UserAuthentication()

    return render(request, 'shop/welcome.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shop:login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
