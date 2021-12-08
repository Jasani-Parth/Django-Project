from django.db import models
from .product import Product
from .customer import Customer
from .transporter import Transporter
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default="", blank=True)
    address2 = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    city = models.CharField(max_length=20,default="", blank=True)
    state = models.CharField(max_length=20,default="", blank=True)
    zip = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    transporter = models.ForeignKey(Transporter, on_delete=models.CASCADE, default=1)

    def placeOrder(self):
        self.save()

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')

    @staticmethod
    def get_all_orders_by_transporter(transporterID):
        return Order.objects.filter(transporter = transporterID)
    
    @staticmethod
    def get_all_orders_by_categoryid_transporter(category_id,transporterID):
        if category_id:
            return Order.objects.filter(transporter=transporterID).filter(category = category_id)
        else:
            return Order.get_all_orders_by_transporter(transporterID)
    
    @staticmethod
    def get_all_orders_by_string_transporterID(search, transporterID):
        if search:
            return Order.objects.filter(transporter = transporterID).filter(name__icontains=search)
        else:
            return Order.get_all_orders_by_transporter(transporterID)