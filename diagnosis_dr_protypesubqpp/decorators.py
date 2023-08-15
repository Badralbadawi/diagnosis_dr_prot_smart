from django.shortcuts import redirect

from django.contrib import messages



# from django.http import HttpResponse




def notLoggedUsers(view_func):
    def wrapper_func(request , *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile_Docor')
        else:
            return view_func(request , *args,**kwargs)
    return wrapper_func


def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group in allowedGroups:
               return view_func(request , *args,**kwargs)
            else:
                return redirect('profile_Docor')
            
        return wrapper_func
    return decorator




def forAdmins(view_func): 
    def wrapper_func(request , *args,**kwargs): 
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Doctor':
            return view_func(request , *args,**kwargs)
        elif group == 'Dr_assint':
            
            return redirect('Profile_assint')
        else:
            return redirect('userlogin')
    return wrapper_func
