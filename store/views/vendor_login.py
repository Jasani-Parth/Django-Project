from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from store.models.vendor import Vendor
from django.views import View


class VendorLogin(View):
    returnUrl = None
    def get(self, request):
        VendorLogin.returnUrl = request.GET.get('returnUrl')
        return render(request, 'vendor_login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        vendor = Vendor.get_vendor_by_email(email)
        error_message = None
        if vendor :
            flag = check_password(password, vendor.password)
            if flag :
                request.session['vendor'] = vendor.id
                if VendorLogin.returnUrl:
                    return HttpResponseRedirect(VendorLogin.returnUrl)
                else:
                    VendorLogin.returnUrl = None
                    return redirect('vendor_homepage')
            else :
                error_message = "Email or Password Invalid !!!"    
        else:
            error_message = "Email or Password Invalid !!!"
        return render(request, 'vendor_login.html', {'error':error_message})

def vendor_logout(request):
    #request.session.clear()
    try:
        del request.session['vendor']
    except KeyError:
        pass
    return redirect('vendor_login')