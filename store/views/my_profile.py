from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from datetime import datetime


class My_Profile(View):
    def get(self, request):
        customerID = request.session.get('customer')
        customer = Customer.objects.get(id=customerID)

        time_now = datetime.now()
        timestamp = dict()

        if time_now.hour < 12:
            timestamp['now'] = "Good Morning."
        elif 12 <= time_now.hour <= 18:
            timestamp['now'] = "Good Afternoon."
        else:
            timestamp['now'] = "Good Evening."

        return render(request, 'my_profile.html', {'customer': customer , 'timestamp' : timestamp})
