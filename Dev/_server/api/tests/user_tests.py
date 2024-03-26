from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase
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


class TestSignIn(APITestCase):
    pass


class TestGetUser(APITestCase):
    pass


class TestUserExpand(APITestCase):
    pass


class TestDeleteUser(APITestCase):
    pass