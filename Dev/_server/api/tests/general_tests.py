from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *


class TestCreateUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/create_user')
        self.view = create_user

    def test_create_user_good(self):
        pass

    def test_create_user_bad(self):
        pass

    def test__create_user_good(self):
        pass

    def test__create_user_bad(self):
        pass


class TestSignIn(APITestCase):
    pass


class TestGetUser(APITestCase):
    pass


class TestUserExpand(APITestCase):
    pass


class TestDeleteUser(APITestCase):
    pass


class TestGetLocationFromAddress(APITestCase):
    pass


class TestGetLocationFromIP(APITestCase):
    pass


class TestLocationsAreNear(APITestCase):
    pass


class TestHaversineDistance(APITestCase):
    pass


class TestWithinDistance(APITestCase):
    pass


class TestGetStores(APITestCase):
    pass


class TestGetActivities(APITestCase):
    pass


class TestGetEvents(APITestCase):
    pass


class TestGetAttractions(APITestCase):
    pass


class TestGetRestaurants(APITestCase):
    pass


class TestCallYelpAPI(APITestCase):
    pass


class TestGetUserLocation(APITestCase):
    pass


class TestNotify(APITestCase):
    pass


class TestUpdateUserLocation(APITestCase):
    pass


