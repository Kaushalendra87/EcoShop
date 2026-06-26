from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'myapp/index.html',{
        'products':products,
        'query': query
    })

def detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'myapp/detail.html', {
        'product':product
    })
