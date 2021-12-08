from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from.models.orders import Order
from .models.review import Review
from .models.order_update import Order_Update_View
from .models.vendor import Vendor
from .models.transporter import Transporter

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

class AdminReview(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'rate', 'created_at']

class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product']

class Admin_Order_Update_View(admin.ModelAdmin):
    list_display = ['id', 'order']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Vendor)
admin.site.register(Transporter)
admin.site.register(Order, AdminOrder)
admin.site.register(Review, AdminReview)
admin.site.register(Order_Update_View, Admin_Order_Update_View)