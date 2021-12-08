from django.db import models
from .customer import Customer
from .product import Product
from .orders import Order

class Order_Update_View(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    update_desc = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)