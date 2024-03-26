from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from Dev._server.api.views import *


class TestCreateUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/create_user')
        self.view = create_user

    def good_test(self):
        pass

    def bad_test(self):
        pass


class TestSignIn(APITestCase):
    pass


class TestGetUser(APITestCase):
    pass


class TestUserExpand(APITestCase):
    pass


class TestDeleteUser(APITestCase):
    pass
