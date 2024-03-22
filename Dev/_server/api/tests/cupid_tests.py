from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *


class TestRateDater(APITestCase):
    pass


class TestGetCupidRating(APITestCase):
    pass


class TestGetCupidAverageRating(APITestCase):
    pass


class TestCupidTransfer(APITestCase):
    pass


class TestGetCupidBalance(APITestCase):
    pass


class TestGetCupidProfile(APITestCase):
    pass


class TestSetCupidProfile(APITestCase):
    pass


class TestAcceptGig(APITestCase):
    pass


class TestCompleteGig(APITestCase):
    pass


class TestDropGig(APITestCase):
    pass


class TestGetGig(APITestCase):
    pass