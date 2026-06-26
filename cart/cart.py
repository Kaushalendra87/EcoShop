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
        
              