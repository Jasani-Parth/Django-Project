from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        if not request.session.get('customer'):
            returnUrl = request.META['PATH_INFO']
            return redirect(f'login?returnUrl={returnUrl}')
 
        response = get_response(request)
        return response

    return middleware