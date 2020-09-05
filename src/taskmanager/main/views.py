from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'comment']


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'comment']


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('index')


def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'products': products})

