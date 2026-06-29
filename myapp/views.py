from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

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
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'myapp/detail.html', {
        'product':product
    })

@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f"Product '{product.name}' added successfully!")
            return redirect('myapp:detail', slug=product.slug)
    else:
        form = ProductForm()

    return render(request, 'myapp/add_product.html', {'form': form})
