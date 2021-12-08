from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    returnUrl = None
    def get(self, request):
        Login.returnUrl = request.GET.get('returnUrl')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer :
            flag = check_password(password, customer.password)
            if flag :
                request.session['customer'] = customer.id
                if Login.returnUrl:
                    return HttpResponseRedirect(Login.returnUrl)
                else:
                    Login.returnUrl = None
                    return redirect('homepage')
            else :
                error_message = "Email or Password Invalid !!!"    
        else:
            error_message = "Email or Password Invalid !!!"
        return render(request, 'login.html', {'error':error_message})

def logout(request):
    try:
        request.session.clear()
    except KeyError:
        pass
    return redirect('homepage')