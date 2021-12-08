from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.review import Review

class ProductView(View):
    def get(self, request):
        productID = request.GET.get('productid')
        product = Product.get_product_by_id(productID)
        related = Product.objects.filter(category=product.category).exclude(id=productID).order_by('-rating')[:4]
        reviews = Review.get_reviews_by_product(product)
        return render(request, 'product.html', {'product':product, 'reviews':reviews, 'related':related})

    def post(self, request):
        productID = request.GET.get('productid')
        customer = request.session.get('customer')
        product = Product.get_product_by_id(productID)
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        Review(customer = Customer(id = customer), product=product, comment=comment, rate=rate).save()
        related = Product.objects.filter(category=product.category).exclude(id=productID).order_by('-rating')[:4]
        reviews = Review.get_reviews_by_product(product)
        total = 0
        count = 0
        for review in reviews:
            total += review.rate
            count += 1
        if(count==0):
            avg = 0
        else :
            avg = total/count
        product.update_rating(avg)
        return render(request, 'product.html', {'product':product, 'reviews':reviews, 'related':related})