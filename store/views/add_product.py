from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.category import Category
from store.models.vendor import Vendor
from store.models.orders import Order


class AddProduct(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'add_product.html', {'categories': categories})

    def post(self, request):
        categories = Category.objects.all()
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_name = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES['image']
        stock = request.POST.get('stock')
        vendorID = request.session.get('vendor')
        vendor = Vendor.objects.get(id=vendorID)
        category = Category.get_category_by_name(category_name)
        # full_image = "uploads/products/"+image
        Product(name=name, price=price, category=category, description=description, image=image, stock=stock,
                vendor=vendor).save()
        return redirect('vendor_homepage')
