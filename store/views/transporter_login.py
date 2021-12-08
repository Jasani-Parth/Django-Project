from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from store.models.vendor import Vendor
from store.models.transporter import Transporter
from django.views import View


class TransporterLogin(View):
    returnUrl = None
    def get(self, request):
        TransporterLogin.returnUrl = request.GET.get('returnUrl')
        return render(request, 'transporter_login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        transporter = Transporter.get_transporter_by_email(email)
        error_message = None
        if transporter :
            flag = check_password(password, transporter.password)
            if flag :
                request.session['transporter'] = transporter.id
                if TransporterLogin.returnUrl:
                    return HttpResponseRedirect(TransporterLogin.returnUrl)
                else:
                    TransporterLogin.returnUrl = None
                    return redirect('transporter_homepage')
            else :
                error_message = "Email or Password Invalid !!!"    
        else:
            error_message = "Email or Password Invalid !!!"
        return render(request, 'transporter_login.html', {'error':error_message})

def transporter_logout(request):
    #request.session.clear()
    try:
        del request.session['transporter']
    except KeyError:
        pass
    return redirect('transporter_login')