from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'products': products})


def add_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_product.html', context)


# изменение данных в бд
def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.quantity = request.POST.get("quantity")
            product.comment = request.POST.get("comment")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/edit.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")



def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
