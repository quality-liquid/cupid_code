import json
import os
import requests

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
    f = open(f'{settings.BASE_DIR}/core/static/manifest.json')
    MANIFEST = json.load(f)


def index(req):
    context = {
        'asset_url': os.environ.get('ASSET_URL', ''),
        'debug': settings.DEBUG,
        'manifest': MANIFEST,
        'js_file': '' if settings.DEBUG else MANIFEST['src/main.ts']['file'],
        'css_file': '' if settings.DEBUG else MANIFEST['src/main.ts']['css'][0]
    }
    return render(req, 'core/index.html', context)


def get_image(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'cupid_logo' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))


def get_menu(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'menu_icon' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))

def get_temp_pfp(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'default_pfp' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))


def get_money(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'money_icon' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))


def get_mic(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'mic_icon' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))


def get_chat(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'chat_icon' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))


def get_emergency(req: HttpRequest):
    FILE_EXTENSION = os.environ.get('FILE_EXTENSION', '')
    VAULT_PATH = os.environ.get('VAULT_PATH', '')
    path = os.path.join(VAULT_PATH, 'emergency_icon' + '.' + FILE_EXTENSION)
    return FileResponse(open(path, "rb"))


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
