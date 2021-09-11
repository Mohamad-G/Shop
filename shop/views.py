from django.shortcuts import render
from .models import category, product


def home(request):
    products = product.objects.all()
    search_text = request.GET.get('search_input')
    if search_text != '' and search_text is not None:
        products = products.filter(title__icontains=search_text)
    return render(request, 'home.html', {'products': products})


def detail(request, id):
    item = product.objects.get(id=id)
    return render(request, 'detail.html', {'item': item})
