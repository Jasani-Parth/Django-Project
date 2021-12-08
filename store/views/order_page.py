from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.orders import Order
from store.models.order_update import Order_Update_View
from store.models.customer import Customer
from store.models.vendor import Vendor
from store.models.transporter import Transporter
from django.views import View

# Create your views here.
class OrderPage(View):
    def get(self, request):
        orderID = request.GET.get('id')
        order = Order.objects.filter(id=orderID).first()
        print(order)
        order_updates = Order_Update_View.objects.filter(order = order)
        return render(request, 'order_page.html', {'order':order, 'order_updates':order_updates})