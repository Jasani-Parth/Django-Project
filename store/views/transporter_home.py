from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.orders import Order
from store.models.customer import Customer
from store.models.vendor import Vendor
from store.models.transporter import Transporter
from django.views import View

# Create your views here.
class TransporterIndex(View):
    def get(self, request):
        transporterID = request.session.get('transporter')
        allorders = Order.get_all_orders_by_transporter(transporterID)
        orders = Order.get_all_orders_by_transporter(transporterID).order_by('status').order_by('date')

        categories = Category.get_all_categories()
        data = {}
        data['orders'] = orders
        data['categories'] = categories
        data['allorders'] = allorders
        return render(request, 'transporter_base.html', data)