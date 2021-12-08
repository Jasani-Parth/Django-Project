from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.category import Category

class ModifyProduct(View):
    def get(self,request):
        productID = request.GET.get('id')
        product = Product.get_product_by_id(productID)
        return redirect('vendor_homepage')

    def post(self,request):
        productID = request.GET.get('id')
        product = Product.get_product_by_id(productID)
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        category_name = request.POST.get('category')
        product.description = request.POST.get('description')
        image = request.POST.get('image')
        product.stock = request.POST.get('stock')
        product.category = Category.get_category_by_name(category_name)
        product.image = "uploads/products/"+image
        product.save()

        return redirect('vendor_homepage')