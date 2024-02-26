from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import requests


def welcome(request):
    render(request, 'registration/index.html')



