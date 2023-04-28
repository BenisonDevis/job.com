from django.shortcuts import redirect,render


def company_login_required(function):
    def wrappeer(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('user_login')
        else:
            if request.user.role != 'COMPANY':
                return render(request, "404.html")
        return function(request,*args,**kwargs)
    return wrappeer