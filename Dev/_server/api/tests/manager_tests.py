import datetime
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
        self.view = views.get_cupids

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
        self.view = views.get_daters

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
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_dater_count')
        self.view = views.get_dater_count
    
    @patch("Dater.objects.all().count")
    def good_test(self, mock_all_daters):
        mock_all_daters.return_value = 1
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data['count'], int)

    @patch("Dater.objects.all().count")
    def bad_test(self, mock_all_daters):
        mock_all_daters.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not isinstance(response.data['count'], int)


class TestGetCupidCount(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_cupid_count')
        self.view = views.get_cupid_count
    
    @patch("Cupid.objects.all().count")
    def good_test(self, mock_all_cupids):
        mock_all_cupids.return_value = 1
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data['count'], int)

    @patch("Cupid.objects.all().count")
    def bad_test(self, mock_all_cupids):
        mock_all_cupids.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not isinstance(response.data['count'], int)


class TestGetActiveCupids(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_active_cupids')
        self.view = views.get_active_cupids

    @patch("helpers.get_sessions")
    def good_test(self, mock_sessions):
        mock_sessions.return_value = {'test': 'test'}
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        mock_sessions.assert_called_once()

    @patch("helpers.get_sessions")
    def bad_test(self, mock_sessions):
        mock_sessions.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_sessions.assert_called_once()   


class TestGetActiveDaters(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_active_daters')
        self.view = views.get_active_daters

    @patch("helpers.get_sessions")
    def good_test(self, mock_sessions):
        mock_sessions.return_value = {'test': 'test'}
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        mock_sessions.assert_called_once()

    @patch("helpers.get_sessions")
    def bad_test(self, mock_sessions):
        mock_sessions.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_sessions.assert_called_once()   


class TestGetGigRates(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_rate')
        self.view = views.get_gig_rate

    @patch("datetime.datetime.now")
    @patch("datetime.timedelta")
    @patch("Gig.objects.filter")
    def good_test(self, mock_datetime, mock_timedelta, mock_gigs):
        mock_datetime.return_value = datetime.datetime.now()
        mock_timedelta.return_value = datetime.timedelta(days=1)
        mock_gigs.return_value = 24
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == "1"

    @patch("datetime.datetime.now")
    @patch("datetime.timedelta")
    @patch("Gig.objects.filter")
    def bad_test(self, mock_datetime, mock_timedelta, mock_gigs):
        mock_datetime.return_value = datetime.datetime.now()
        mock_timedelta.return_value = datetime.timedelta(days=1)
        mock_gigs.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestGetGigCount(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_count')
        self.view = views.get_gig_count

    @patch("Gig.objects.all().count")
    def good_test(self, mock_gigs):
        mock_gigs.return_value = 1
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        mock_gigs.assert_called_once()

    @patch("Gig.objects.all().count")
    def bad_test(self, mock_gigs):
        mock_gigs.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_gigs.assert_called_once()


class TestGetGigDropRate(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_drop_rate')
        self.view = views.get_gig_drop_rate

    @patch("datetime.datetime.now")
    @patch("datetime.timedelta")
    @patch("Gig.objects.filter")
    def good_test(self, mock_datetime, mock_timedelta, mock_gigs):
        mock_datetime.return_value = datetime.datetime.now()
        mock_timedelta.return_value = datetime.timedelta(days=1)
        mock_gigs.return_value = 24
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == "1"

    @patch("datetime.datetime.now")
    @patch("datetime.timedelta")
    @patch("Gig.objects.filter")
    def bad_test(self, mock_datetime, mock_timedelta, mock_gigs):
        mock_datetime.return_value = datetime.datetime.now()
        mock_timedelta.return_value = datetime.timedelta(days=1)
        mock_gigs.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestGetGigCompleteRate(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig_complete_rate')
        self.view = views.get_gig_complete_rate

    @patch("datetime.datetime.now")
    @patch("datetime.timedelta")
    @patch("Gig.objects.filter")
    def good_test(self, mock_datetime, mock_timedelta, mock_gigs):
        mock_datetime.return_value = datetime.datetime.now()
        mock_timedelta.return_value = datetime.timedelta(days=1)
        mock_gigs.return_value = 24
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == "1"

    @patch("datetime.datetime.now")
    @patch("datetime.timedelta")
    @patch("Gig.objects.filter")
    def bad_test(self, mock_datetime, mock_timedelta, mock_gigs):
        mock_datetime.return_value = datetime.datetime.now()
        mock_timedelta.return_value = datetime.timedelta(days=1)
        mock_gigs.return_value = None
        request = self.factory.post(self.url)
        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestSuspend(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/suspend')
        self.view = views.suspend

    @patch("get_object_or_404")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def good_test(self, mock_404, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_404.return_value = MagicMock()
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
        
    @patch("get_object_or_404")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def bad_test(self, mock_404, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_404.return_value = MagicMock()
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
        mock_dater_serializer.return_value = Response(status=HTTP_404_NOT_FOUND)

        user_data = {'role': 'Dater'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_dater_serializer.assert_called_once()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_not_called()

        # Test 3: Cupid model is bad
        mock_cupid_serializer.return_value = Response(status=HTTP_404_NOT_FOUND)

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

    @patch("get_object_or_404")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def good_test(self, mock_404, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_404.return_value = MagicMock()
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
        
    @patch("get_object_or_404")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch("helpers.retrieved_response")
    def bad_test(self, mock_404, mock_dater_serializer, mock_cupid_serializer, mock_response):
        mock_404.return_value = MagicMock()
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
        mock_dater_serializer.return_value = Response(status=HTTP_404_NOT_FOUND)

        user_data = {'role': 'Dater'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_dater_serializer.assert_called_once()
        mock_cupid_serializer.assert_not_called()
        mock_response.assert_not_called()

        # Test 3: Cupid model is bad
        mock_cupid_serializer.return_value = Response(status=HTTP_404_NOT_FOUND)

        user_data = {'role': 'Cupid'}
        request = self.factory.post(self.url)
        request.data = user_data
        response = self.view(request)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_dater_serializer.assert_not_called()
        mock_cupid_serializer.assert_called_once()
        mock_response.assert_not_called()