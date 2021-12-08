from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.order_update import Order_Update_View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderUpdate(View):
    def get(self, request):
        orderID = request.GET.get('order')
        order = Order.objects.get(id=orderID)
        order_updates = Order_Update_View.objects.filter(order = order)
        return render(request, 'tracker.html', {'order':order, 'order_updates':order_updates})