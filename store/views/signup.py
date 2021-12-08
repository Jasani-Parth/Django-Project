from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
    
        # saving
        error_message = None
        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else :
            return render(request, 'signup.html', {'error':error_message})   

    def validateCustomer(self, customer):
    # validation
        error_message = None
        if(not customer.first_name):
            error_message = "First Name Required"
        elif len(customer.first_name) < 3:
                error_message = "First Name must be atleast 3 characters long"
        elif(not customer.last_name):
            error_message = "Last Name Required"
        elif len(customer.last_name) < 3:
                error_message = "Last Name must be atleast 3 characters long"
        elif (not customer.phone):
            error_message = "Phone Number Required"
        elif (len(customer.phone) < 10):
            error_message = "Phone Number must be 10 characters long"
        elif len(customer.email)<5 :
            error_message = "Email must be longer than 5 characters"
        elif len(customer.password)<6 :
            error_message = "Password must be atleast 6 characters long"
        elif (customer.isExists()):
            error_message = "Email ID already exists"

        return error_message

   


