from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.vendor import Vendor
from django.views import View

# Create your views here.
class VendorIndex(View):
    def get(self, request):
        categoryID = request.GET.get('category')
        search = request.GET.get('search')
        vendorID = request.session.get('vendor')
        allproducts = Product.get_all_products_by_vendor(vendorID)
        if categoryID:
            products = Product.get_all_products_by_categoryid_vendor(categoryID,vendorID).order_by('-rating')
        elif search:
            products = Product.get_all_products_by_string_vendorID(search,vendorID).order_by('-rating')
        else:
            products = Product.get_all_products_by_vendor(vendorID)

        categories = Category.get_all_categories()
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['allproducts'] = allproducts
        return render(request, 'vendor_base.html', data)