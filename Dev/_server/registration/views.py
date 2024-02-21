from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse



def welcome(req):
    render(req, 'registration/index.html')

#TODO: Create User
def sign_up(req):
    if req.method == 'POST':
        user = User.objects.create_user(
            
        )
        login(req, user)
        return redirect('/')
    else:
        return render(req, 'registration/sign_up.html')

#TODO: Ensure the authenticate is what we want to use
def sign_in(req):
    if req.method == 'POST':
        user = authenticate(req, username=req.POST.get('email'), password=req.POST.get('password'))
        if user is not None:
            login(req, user)
            return redirect('/')

        return render(req, 'registration/sign_in.html')
    else:
        return render(req, 'registration/sign_in.html')

def logout_view(request):
    logout(request)
    return JsonResponse({'success': True })
