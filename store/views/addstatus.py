from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.transporter import Transporter
from store.models.order_update import Order_Update_View


class AddStatus(View):
    def post(self, request):
        orderID = request.GET.get('id')
        order = Order.objects.filter(id=orderID).first()
        desc = request.POST.get('status')
        delivery = request.POST.get('delivery')
        if delivery == "Pending":
            order.status = False
        else:
            order.status = True
        order.save()
        order_update = Order_Update_View(order=order, update_desc=desc)
        order_update.save()

        order_updates = Order_Update_View.objects.filter(order=order)
        return render(request, 'order_page.html', {'order': order, 'order_updates': order_updates})
