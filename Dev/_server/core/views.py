from django.shortcuts import render, redirect
from django.conf import settings
import json
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import JsonResponse
import requests
from django.http import HttpRequest
from django.http import FileResponse


# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f'{settings.BASE_DIR}/core/static/manifest.json')
    MANIFEST = json.load(f)



# Create your views here.
def index(req):
    context = {
        'asset_url': os.environ.get('ASSET_URL', ''),
        'debug': settings.DEBUG,
        'manifest': MANIFEST,
        'js_file': '' if settings.DEBUG else MANIFEST['src/main.ts']['file'],
        'css_file': '' if settings.DEBUG else MANIFEST['src/main.ts']['css'][0]
    }
    return render(req, 'core/index.html', context)

def sign_up(request):
    if request.method == 'POST':
        user = requests.post('http://localhost:8000/api/user/create/', data=request.POST)
        login(request, user)
    return redirect('/')

def sign_in(request):
    if request.method == 'POST':
        user = requests.get(f'http://localhost:8000/api/user/', data=request.POST)
        if user is not None:
            login(request, user)
    return redirect('/')

def get_image(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'cupid_logo' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))


@login_required
def logout_view(request):
    try:
        logout(request)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
