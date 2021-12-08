from django.db import models
from .customer import Customer
from .product import Product


class Review(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    comment = models.CharField(max_length=250)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_reviews_by_product(product):
        return Review.objects.filter(product = product)

    def __str__(self):
        return str(self.id)

