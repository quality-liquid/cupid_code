from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *


class TestUser(TestCase):
    pass


class TestDater(TestCase):
    pass


class TestCupid(TestCase):
    pass


class TestMessage(TestCase):
    pass


class TestQuest(TestCase):
    pass


class TestGig(TestCase):
    pass


class TestDate(TestCase):
    pass


class TestFeedback(TestCase):
    pass


class TestPaymentCard(TestCase):
    pass


class TestBankAccount(TestCase):
    pass
