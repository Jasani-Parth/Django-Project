from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.transporter import Transporter
from store.models.order_update import Order_Update_View

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))
        transporter = Transporter.get_random()
        
        for product in products:
            order = Order(customer = Customer(id = customer), product = product, quantity = cart.get(str(product.id)), price = product.price, address = address, address2 = address2, phone = phone, city = city, state = state, zip = zip, transporter = transporter)
            order.placeOrder()
            update = Order_Update_View(order=order, update_desc="Your Order has been placed successfully !!!")
            update.save()
            product.stock = product.stock - cart.get(str(product.id))
            product.save()
        
        request.session['cart'] = {}
        return redirect('cart')