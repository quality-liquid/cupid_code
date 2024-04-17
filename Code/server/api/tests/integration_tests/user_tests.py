from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Code.server.api.views import *

from serializers import (
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
from models import (User, Dater, Cupid, Gig, Quest, Message, Date, Feedback, PaymentCard, BankAccount)
import helpers
import views


class TestCreateUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/create_user')
        self.view = views.create_user

    @patch("UserSerializer")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch('helpers.update_location')
    def good_test(self, mock_user, mock_dater, mock_cupid, mock_update_location):
        mock_user.return_value = MagicMock()
        mock_dater.return_value = MagicMock()
        mock_cupid.return_value = MagicMock()
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'user_id': 1, 'location': 'Test', 'role': 'dater', 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_201_CREATED
        mock_user.assert_called_once()
        mock_dater.assert_called_once()
        mock_cupid.assert_not_called()

    @patch("UserSerializer")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch('helpers.update_location')
    def bad_test(self, mock_user, mock_dater, mock_cupid, mock_update_location):
        mock_user.return_value = MagicMock()
        mock_dater.return_value = MagicMock()
        mock_cupid.return_value = MagicMock()
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'user_id': 1, 'location': 'Test', 'role': None, 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['error'] == 'invalid user type'
        mock_user.assert_called_once()
        mock_dater.assert_not_called()
        mock_cupid.assert_not_called()

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

class TestGetUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_user')
        self.view = views.get_user

    @patch("helpers.initialize_serializer")
    @patch("helpers.user_expand")
    def good_test(self, mock_serializer, mock_user_expand):
        mock_serializer.return_value = MagicMock()
        mock_user_expand.return_value = "Test User Data"
        request = self.factory.post(self.url)
        request.data["user_id"] = 1
        request.data["is_staff"] = True

        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_serializer.assert_called_once()
        mock_user_expand.assert_called_once()
    
    @patch("helpers.initialize_serializer")
    @patch("helpers.user_expand")
    def bad_test(self, mock_serializer, mock_user_expand):
        mock_serializer.return_value = MagicMock()
        mock_user_expand.return_value = "Test User Data"
        request = self.factory.post(self.url)
        request.data["user_id"] = 1
        request.data["is_staff"] = False

        response = self.view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        mock_serializer.assert_not_called()
        mock_user_expand.assert_not_called()


class TestUserExpand(APITestCase):
    @patch("UserSerializer")
    def good_test(self, mock_serializer):
        mock_serializer.return_value = MagicMock()
        user = MagicMock()
        serializer = MagicMock()
        user.role = User.Role.MANAGER
        serializer.data = {'test': 'test'}
        return_data = helpers.user_expand(user, serializer)
        assert return_data['user'] == {'test': 'test'}
        assert return_data['user']['password'] == None
        
        user.role = User.Role.CUPID
        return_data = helpers.user_expand(user, serializer)
        assert return_data['user'] == {'test': 'test'}
        assert return_data['user']['password'] == None

    @patch("UserSerializer")
    def bad_test(self, mock_serializer):
        mock_serializer.return_value = MagicMock
        user = 3
        other_serializer = MagicMock()
        response = user_expand(user, other_serializer)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_serializer.assert_called_once()

        
class TestDeleteUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/delete_user')
        self.view = views.delete_user

    def good_test(self):
        request = self.factory.post(self.url)
        request.data["user_id"] = 1
        request.data["is_staff"] = True

        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        request = self.factory.post(self.url)
        request.data["user_id"] = 1
        request.data["is_staff"] = False

        response = self.view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN

