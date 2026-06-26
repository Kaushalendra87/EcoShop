from django.shortcuts import render
from django.http import JsonResponse
from .cart import Cart
from myapp.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def cart_add(request):
    cart = Cart(request)
    print("Add to cart button clicked")
    if request.method == 'POST':
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("Product added to the cart has the id of :",product_id)
        print("Product added to the cart has the quantity of :",product_quantity)
        # product = Product.objects.get(id=product_id)
        product = get_object_or_404(Product,id=product_id)
        cart.add(product=product, product_qty=product_quantity)
    return JsonResponse({'qty': len(cart)})

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart_summary.html', {'cart': cart})

def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart.delete(product_id=product_id)
        
        cart_total = cart.get_total()
        cart_qty = len(cart)
        
        return JsonResponse({
            'qty': cart_qty,
            'total': cart_total
        })
    return JsonResponse({'error': 'Invalid request'})