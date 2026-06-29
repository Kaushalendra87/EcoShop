from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from myapp.models import Product
from .models import Order, OrderItem
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Create your views here.
def cart_add(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=403)
        
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
    return JsonResponse({'qty': len(cart)})

@login_required
def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart_summary.html', {'cart': cart})

def cart_delete(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=403)
        
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

@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your cart is empty. Add items to checkout.")
        return redirect('cart_summary')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total()
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['qty']
                )

            # Clear cart session
            if 'cart' in request.session:
                del request.session['cart']
                request.session.modified = True

            messages.success(request, f"Order #{order.id} placed successfully!")
            return redirect('order_success', order_id=order.id)
    else:
        initial_data = {
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        }
        form = CheckoutForm(initial=initial_data)

    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'form': form
    })

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cart/order_success.html', {'order': order})

@user_passes_test(lambda u: u.is_superuser)
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'cart/admin_orders.html', {'orders': orders})