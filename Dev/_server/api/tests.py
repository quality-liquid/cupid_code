from django.test import TestCase
from rest_framework.test import APIRequestFactory
from unittest.mock import patch, MagicMock
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import *
from .views import *

