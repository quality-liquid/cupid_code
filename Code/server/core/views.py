from json import load as load_json
from os import environ as env 
from os.path import join as join_path
# import requests TODO delete me later if still not used when time for deployment

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.http import HttpRequest
from django.http import FileResponse

from api.models import User
# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f'{settings.BASE_DIR}/core/static/core/.vite/manifest.json')
    MANIFEST = load_json(f)


def index(req):
    context = {
        'asset_url': env.get('ASSET_URL', ''),
        'debug': settings.DEBUG,
        'manifest': MANIFEST,
        'js_file': '' if settings.DEBUG else MANIFEST['src/main.ts']['file'],
        'css_file': '' if settings.DEBUG else MANIFEST['src/main.ts']['css'][0]
    }
    return render(req, 'core/index.html', context)


def get_image(req: HttpRequest):
    FILE_EXTENSION = env.get('FILE_EXTENSION', '')
    VAULT_PATH = env.get('VAULT_PATH', '')
    path = join_path(VAULT_PATH, 'cupid_logo' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))

def get_graph(req: HttpRequest):
    FILE_EXTENSION = env.get('FILE_EXTENSION', '')
    VAULT_PATH = env.get('VAULT_PATH', '')
    path = join_path(VAULT_PATH, 'graph' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
