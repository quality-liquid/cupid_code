from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *


class TestUserSerializer(TestCase):
    pass


class TestDaterSerializer(TestCase):
    pass


class TestCupidSerializer(TestCase):
    pass


class TestManagerSerializer(TestCase):
    pass


class TestMessageSerializer(TestCase):
    pass


class TestGigSerializer(TestCase):
    pass


class TestQueueSerializer(TestCase):
    pass


class TestDateSerializer(TestCase):
    pass


class TestFeedbackSerializer(TestCase):
    pass


class TestPaymentSerializer(TestCase):
    pass


class TestBankAccountSerializer(TestCase):
    pass