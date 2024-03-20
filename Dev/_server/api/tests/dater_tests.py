from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *


class TestGetAIResponse(APITestCase):
    pass


class TestSendChatMessage(APITestCase):
    pass


class TestGetFiveMessages(APITestCase):
    pass


class TestCalendar(APITestCase):
    pass

class TestGetDaterRating(APITestCase):
    pass


class TestGetDaterAverageRating(APITestCase):
    pass


class TestDaterTransfer(APITestCase):
    pass


class TestGetDaterBalance(APITestCase):
    pass


class TestGetDaterProfile(APITestCase):
    pass


class TestSetDaterProfile(APITestCase):
    pass


class TestRateCupid(APITestCase):
    pass


class TestCreateGig(APITestCase):
    pass


class TestSpeechToText(APITestCase):
    pass
