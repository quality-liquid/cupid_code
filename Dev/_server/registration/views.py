from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import requests


def welcome(request):
    render(request, 'registration/index.html')


def sign_up(request):
    if request.method == 'POST':
        user = requests.post('http://localhost:8000/api/user/create/', data=request.POST)
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'registration/sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        user = requests.get(f'http://localhost:8000/api/user/', data=request.POST)
        if user is not None:
            login(request, user)
            return redirect('/')
        return render(request, 'registration/sign_in.html')
    else:
        return render(request, 'registration/sign_in.html')


@login_required
def logout_view(request):
    try:
        logout(request)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
