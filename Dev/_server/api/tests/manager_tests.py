from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *

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
        self.view = views.get_cupids()

    @patch("Cupid.objects.all")
    @patch("CupidSerializer")
    def good_test(self, mock_all_cupids, mock_serializer):
        mock_all_cupids.return_value = MagicMock()
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_all_cupids.assert_called_once()
        mock_serializer.assert_called_once()

    @patch("Cupid.objects.all")
    @patch("CupidSerializer")
    def bad_test(self, mock_all_cupids, mock_serializer):
        # Test 1: Testing if Cupid.objects.all gives back nothing
        mock_all_cupids.return_value = None
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_all_cupids.assert_called_once()
        mock_serializer.assert_not_called()    

        # Test 2: Testing if CupidSerializer gives back nothing
        mock_all_cupids.return_value = MagicMock()
        mock_serializer.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_all_cupids.assert_called_once()
        mock_serializer.assert_called_once() 

class TestGetDaters(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_daters')
        self.view = views.get_daters()

    @patch("Dater.objects.all")
    @patch("DaterSerializer")
    def good_test(self, mock_all_daters, mock_serializer):
        mock_all_daters.return_value = MagicMock()
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_all_daters.assert_called_once()
        mock_serializer.assert_called_once()

    @patch("Dater.objects.all")
    @patch("DaterSerializer")
    def bad_test(self, mock_all_daters, mock_serializer):
        # Test 1: Testing if Dater.objects.all gives back nothing
        mock_all_daters.return_value = None
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_all_daters.assert_called_once()
        mock_serializer.assert_not_called()    

        # Test 2: Testing if DaterSerializer gives back nothing
        mock_all_daters.return_value = MagicMock()
        mock_serializer.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'test': 'test'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_all_daters.assert_called_once()
        mock_serializer.assert_called_once() 


class TestGetDaterCount(APITestCase):
    pass


class TestGetCupidCount(APITestCase):
    pass


class TestGetActiveCupids(APITestCase):
    pass


class TestGetActiveDaters(APITestCase):
    pass


class TestGetGigRates(APITestCase):
    pass


class TestGetGigCount(APITestCase):
    pass


class TestGetGigDropRate(APITestCase):
    pass


class TestGetGigCompleteRate(APITestCase):
    pass


class TestSuspend(APITestCase):
    pass


class TestUnsuspend(APITestCase):
    pass
