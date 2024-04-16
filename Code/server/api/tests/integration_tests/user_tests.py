from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from Code.server.api.serializers import (
    UserSerializer,
    DaterSerializer,
    CupidSerializer,
    ManagerSerializer,
    MessageSerializer,
    GigSerializer,
    DateSerializer,
    FeedbackSerializer,
    PaymentCardSerializer,
    BankAccountSerializer,
    QuestSerializer,
)
from Code.server.api.models import (User, Dater, Cupid, Gig, Quest, Message, Date, Feedback, PaymentCard, BankAccount)
import Code.server.api.helpers as helpers
import Code.server.api.views as views


class TestCreateUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/create_user')
        self.view = views.create_user

    @patch('helpers.update_location')
    def good_test(self, mock_update_location):
        mock_update_location.return_value = None
        request = self.factory.post(self.url)

        request.data = {'user_id': 1, 'location': 'Test', 'role': 'dater', 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_201_CREATED

    @patch('helpers.update_location')
    def bad_test(self, mock_update_location):
        mock_update_location.return_value = None
        request = self.factory.post(self.url)

        request.data = {'user_id': 1, 'location': 'Test', 'role': None, 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['error'] == 'invalid user type'


class TestSignIn(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/sign_in')
        self.view = views.sign_in

    @patch('helpers.update_location')
    def good_test(self, mock_update_location):
        mock = MagicMock()
        mock.user_id = 1
        mock.username = "Test"
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        force_authenticate(request, user=self.user)

        request.data = {'user_id': 1, 'location': 'Test', 'role': 'dater', 'phone_number': '1123456789',
                        'username': 'Test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_update_location.assert_called_once()

    @patch('helpers.update_location')
    def bad_test(self, mock_update_location):
        mock = MagicMock()
        mock.user_id = 1
        mock.username = None
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        force_authenticate(request, user=self.user)

        request.data = {'user_id': 1, 'location': 'Test', 'role': 'dater', 'phone_number': '1123456789',
                        'username': None}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BADD_REQUEST
        mock_update_location.assert_called_once()
