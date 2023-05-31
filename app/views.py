from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from app.form import CreateUserForm
from app.models import Product


class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.all()


class Categories(ListView):
    model = Product
    template_name = 'categories.html'
    queryset = Product.objects.all()


def contact(request):
    return render(request, 'contact.html')


class Single(DetailView):
    model = Product
    template_name = 'single.html'


def confirm(request):
    return render(request, 'confirm_shop.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}

    return render(request, 'registration/login.html', context)