from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.vendor import Vendor
from store.models.transporter import Transporter
from django.views import View

class TransporterSignup(View):
    def get(self, request):
        return render(request, 'transporter_signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        transporter = Transporter(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
    
        # saving
        error_message = None
        error_message = self.validateTransporter(transporter)
        if not error_message:
            transporter.password = make_password(transporter.password)
            transporter.register()
            return redirect('transporter_login')
        else :
            return render(request, 'transporter_signup.html', {'error':error_message})   

    def validateTransporter(self, transporter):
    # validation
        error_message = None
        if(not transporter.first_name):
            error_message = "First Name Required"
        elif len(transporter.first_name) < 3:
                error_message = "First Name must be atleast 3 characters long"
        elif(not transporter.last_name):
            error_message = "Last Name Required"
        elif len(transporter.last_name) < 3:
                error_message = "Last Name must be atleast 3 characters long"
        elif (not transporter.phone):
            error_message = "Phone Number Required"
        elif (len(transporter.phone) < 10):
            error_message = "Phone Number must be 10 characters long"
        elif len(transporter.email)<5 :
            error_message = "Email must be longer than 5 characters"
        elif len(transporter.password)<6 :
            error_message = "Password must be atleast 6 characters long"
        elif (transporter.isExists()):
            error_message = "Email ID already exists"

        return error_message

   


