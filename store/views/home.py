from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categoryID = request.GET.get('category')
        search = request.GET.get('search')
        min_price = request.GET.get('min')
        max_price = request.GET.get('max')
        allproducts = Product.get_all_products()
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID).order_by('-rating')
        elif search:
            products = Product.get_all_products_by_string(search).order_by('-rating')
        elif min_price:
            products=Product.objects.filter(price__range=(min_price,max_price))
        else:
            products = Product.get_all_products()

        categories = Category.get_all_categories()
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['allproducts'] = allproducts
        return render(request, 'index.html', data)
    
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if(quantity<=1):
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('homepage')

