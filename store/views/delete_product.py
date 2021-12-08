from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order

class DeleteProduct(View):
    def get(self,request):
        productID = request.GET.get('id')
        product = Product.get_product_by_id(productID)
        product.delete()
        return redirect('vendor_homepage')