from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.vendor import Vendor
from django.views import View

class VendorSignup(View):
    def get(self, request):
        return render(request, 'vendor_signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        vendor = Vendor(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
    
        # saving
        error_message = None
        error_message = self.validateVendor(vendor)
        if not error_message:
            vendor.password = make_password(vendor.password)
            vendor.register()
            return redirect('vendor_login')
        else :
            return render(request, 'vendor_signup.html', {'error':error_message})   

    def validateVendor(self, vendor):
    # validation
        error_message = None
        if(not vendor.first_name):
            error_message = "First Name Required"
        elif len(vendor.first_name) < 3:
                error_message = "First Name must be atleast 3 characters long"
        elif(not vendor.last_name):
            error_message = "Last Name Required"
        elif len(vendor.last_name) < 3:
                error_message = "Last Name must be atleast 3 characters long"
        elif (not vendor.phone):
            error_message = "Phone Number Required"
        elif (len(vendor.phone) < 10):
            error_message = "Phone Number must be 10 characters long"
        elif len(vendor.email)<5 :
            error_message = "Email must be longer than 5 characters"
        elif len(vendor.password)<6 :
            error_message = "Password must be atleast 6 characters long"
        elif (vendor.isExists()):
            error_message = "Email ID already exists"

        return error_message

   


