from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.category import Category

class ModifyProductForm(View):
    def get(self,request):
        id = request.GET.get('id')
        categories = Category.objects.all()
        return render(request, 'modify_product_form.html', {'id':id,'categories':categories})

    def post(self,request):
        id = request.GET.get('id')
        categories = Category.objects.all()
        return render(request, 'modify_product_form.html', {'id':id,'categories':categories})