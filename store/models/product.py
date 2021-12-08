from django.db import models
from .category import Category
from .vendor import Vendor

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    rating = models.DecimalField(default=0.0,max_digits=2, decimal_places=1)
    stock = models.IntegerField(default=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def update_rating(self,rating):
        self.rating = rating
        self.save()

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_vendor(vendorID):
        return Product.objects.filter(vendor=vendorID)

    @staticmethod
    def get_product_by_id(id):
        return Product.objects.get(id=id)

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
    
    @staticmethod
    def get_all_products_by_categoryid_vendor(category_id,vendorID):
        if category_id:
            return Product.objects.filter(vendor=vendorID).filter(category = category_id)
        else:
            return Product.get_all_products_by_vendor(vendorID)
    
    @staticmethod
    def get_all_products_by_string(search):
        if search:
            return Product.objects.filter(name__icontains=search)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_string_vendorID(search, vendorID):
        if search:
            return Product.objects.filter(vendor=vendorID).filter(name__icontains=search)
        else:
            return Product.get_all_products_by_vendor(vendorID)