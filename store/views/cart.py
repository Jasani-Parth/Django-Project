from django.views import View
from django.shortcuts import redirect, render
from store.models.product import Product

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_ids(ids)
        allproducts = Product.get_all_products()
        return render(request, 'cart.html', {'products':products,'allproducts':allproducts})