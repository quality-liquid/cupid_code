from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *


class TestGetCupids(APITestCase):
    pass


class TestGetDaters(APITestCase):
    pass


class TestGetDaterCount(APITestCase):
    pass


class TestGetCupidCount(APITestCase):
    pass


class TestGetActiveCupids(APITestCase):
    pass


class TestGetActiveDaters(APITestCase):
    pass


class TestGetGigRates(APITestCase):
    pass


class TestGetGigCount(APITestCase):
    pass


class TestGetGigDropRate(APITestCase):
    pass


class TestGetGigCompleteRate(APITestCase):
    pass


class TestSuspend(APITestCase):
    pass


class TestUnsuspend(APITestCase):
    pass
