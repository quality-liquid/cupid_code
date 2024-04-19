import datetime
from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Code.server.api.models import *
from Code.server.api.views import *

import views
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


class TestGetCupids(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_cupids')
        self.view = views.get_cupids

    @patch("CupidSerializer")
    def good_test(self, mock_serializer):
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_serializer.assert_called_once()

    @patch("CupidSerializer")
    def bad_test(self, mock_serializer):
        # Test 1: Testing if Cupid.objects.all gives back nothing
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_serializer.assert_not_called()    

        # Test 2: Testing if CupidSerializer gives back nothing
        mock_serializer.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_serializer.assert_called_once() 


class TestGetDaters(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_daters')
        self.view = views.get_daters

    @patch("DaterSerializer")
    def good_test(self, mock_serializer):
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_serializer.assert_called_once()

    @patch("DaterSerializer")
    def bad_test(self, mock_serializer):
        # Test 1: Testing if Dater.objects.all gives back nothing
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_serializer.assert_not_called()    

        # Test 2: Testing if DaterSerializer gives back nothing
        mock_serializer.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_serializer.assert_called_once() 


class TestGetDaterCount(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_dater_count')
        self.view = views.get_dater_count
    
    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data['count'], int)

    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not isinstance(response.data['count'], int)


class TestGetCupidCount(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_cupid_count')
        self.view = views.get_cupid_count
    
    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data['count'], int)

    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not isinstance(response.data['count'], int)


class TestGetActiveCupids(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_active_cupids')
        self.view = views.get_active_cupids

    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestGetActiveDaters(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_active_daters')
        self.view = views.get_active_daters

    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

class TestGetGigRates(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_rate')
        self.view = views.get_gig_rate

    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK


    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestGetGigCount(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_count')
        self.view = views.get_gig_count

    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

class TestGetGigDropRate(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_drop_rate')
        self.view = views.get_gig_drop_rate

    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestGetGigCompleteRate(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_complete_rate')
        self.view = views.get_gig_complete_rate

    def good_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestSuspend(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/suspend')
        self.view = views.suspend

    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def good_test(self, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_dater_serializer.return_value = MagicMock()
        mock_cupid_serializer.return_value = MagicMock()
        mock_response = MagicMock()

        user_data = {'role': 'Dater'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_dater_serializer.assert_called_once()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_called_once()
        
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def bad_test(self, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_dater_serializer.return_value = MagicMock()
        mock_cupid_serializer.return_value = MagicMock()
        mock_response = MagicMock()

        # Test 1: Role is bad
        user_data = {'role': None}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_dater_serializer.assert_not_called()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_not_called()

        # Test 2: Dater model is bad
        mock_dater_serializer.return_value = Response(status=status.HTTP_404_NOT_FOUND)

        user_data = {'role': 'Dater'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_dater_serializer.assert_called_once()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_not_called()

        # Test 3: Cupid model is bad
        mock_cupid_serializer.return_value = Response(status=status.HTTP_404_NOT_FOUND)

        user_data = {'role': 'Cupid'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_dater_serializer.assert_not_called()
        mock_cupid_serializer.assert_called_once()
        mock_response.assert_not_called()

class TestUnsuspend(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/unsuspend')
        self.view = views.unsuspend

    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def good_test(self, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_dater_serializer.return_value = MagicMock()
        mock_cupid_serializer.return_value = MagicMock()
        mock_response = MagicMock()

        user_data = {'role': 'Dater'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_dater_serializer.assert_called_once()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_called_once()
        
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def bad_test(self, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_dater_serializer.return_value = MagicMock()
        mock_cupid_serializer.return_value = MagicMock()
        mock_response = MagicMock()

        # Test 1: Role is bad
        user_data = {'role': None}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_dater_serializer.assert_not_called()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_not_called()

        # Test 2: Dater model is bad
        mock_dater_serializer.return_value = Response(status=status.HTTP_404_NOT_FOUND)

        user_data = {'role': 'Dater'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_dater_serializer.assert_called_once()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_not_called()

        # Test 3: Cupid model is bad
        mock_cupid_serializer.return_value = Response(status=status.HTTP_404_NOT_FOUND)

        user_data = {'role': 'Cupid'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_dater_serializer.assert_not_called()
        mock_cupid_serializer.assert_called_once()
        mock_response.assert_not_called()