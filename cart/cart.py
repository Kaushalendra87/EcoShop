from myapp.models import Product

class Cart():
    def __init__(self,request):
        self.session = request.session
        cart = request.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart']={}
        self.cart = cart

    def add (self,product,product_qty):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] += int(product_qty)
        else:
            self.cart[product_id] = {'price':str(product.price), 'qty':int(product_qty)} 
        self.session.modified = True

    def __len__(self):
        return sum(int(item.get('qty', 0)) for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            if 'product' in item:
                item['price'] = float(item['price'])
                item['total_price'] = item['price'] * item['qty']
                yield item

    def get_total(self):
        return sum(float(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
        
              