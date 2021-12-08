from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.review import Review
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Reviews(View):
    def get(self, request):
        productID = request.GET.get('productid')
        product = Product.objects.get(id=productID)
        reviews = Review.get_reviews_by_product(product)
        return render(request, 'product.html', {'reviews':reviews})