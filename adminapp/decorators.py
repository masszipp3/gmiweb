from django.shortcuts import redirect,render

def auth_admin(func):
    def wrap(request, *args, **kwargs):
        if 'adminid' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('adminapp:adminlogin')
            
    return wrap