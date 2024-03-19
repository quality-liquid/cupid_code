from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from .models import *
from .views import *


class TestCreateUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/create_user')
        self.view = create_user

    @patch('User.objects')
    @patch('UserSerializer')
    @patch('DaterSerializer')
    @patch('CupidSerializer')
    def test_create_user_good(
            self, mock_user_objects, mock_user_serializer,
            mock_dater_serializer, mock_cupid_serializer
    ):
        # Test 1: create dater
        # set up mocks
        mock_user_objects.get.return_value = MagicMock()
        mock_user_objects.delete.return_value = None
        mock_user_serializer.is_valid.return_value = True
        mock_user_serializer.save.return_value = None
        mock_dater_serializer.is_valid.return_value = True
        mock_dater_serializer.save.return_value = None
        # set up request
        data = {
            'username': 'test',
            'password': 'test',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test',
            'role': 'Dater',
        }
        request = self.factory.post(self.url, data)
        request.META['REMOTE_ADDR'] = '1.1.1.1'
        # make request
        response = self.view(request)
        # test response and mocks
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert mock_user_serializer.called
        assert mock_dater_serializer.called
        assert not mock_cupid_serializer.called
        assert mock_user_serializer.save.called
        assert mock_dater_serializer.save.called

        # Test 2: create cupid
        # set up mocks
        mock_user_objects.get.return_value = MagicMock()
        mock_user_objects.delete.return_value = None
        mock_user_serializer.is_valid.return_value = True
        mock_user_serializer.save.return_value = None
        mock_cupid_serializer.is_valid.return_value = True
        mock_cupid_serializer.save.return_value = None
        # set up request
        data = {
            'username': 'test',
            'password': 'test',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test',
            'role': 'Cupid',
        }
        request = self.factory.post(self.url, data)
        request.META['REMOTE_ADDR'] = '1.1.1.1'
        # make request
        response = self.view(request)
        # test response and mocks
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert mock_user_serializer.called
        assert mock_cupid_serializer.called
        assert not mock_dater_serializer.called
        assert mock_user_serializer.save.called
        assert mock_cupid_serializer.save.called

    @patch('User.objects')
    @patch('UserSerializer')
    @patch('DaterSerializer')
    @patch('CupidSerializer')
    def test_create_user_bad(self):
        # Test 1: missing username
        data = {
            'password': 'test',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test'
        }
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test 2: missing password
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test'
        }
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test 3: missing email
        data = {
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test'
        }
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test 4: not unique username
        data = {
            'username': 'test',
            'password': 'test',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test'
        }
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test 5: not unique email
        data = {
            'username': 'test',
            'password': 'test',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test'
        }
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestSignIn(APITestCase):
    pass


class TestGetUser(APITestCase):
    pass


class TestUserExpand(APITestCase):
    pass


class TestDeleteUser(APITestCase):
    pass


class TestSendChatMessage(APITestCase):
    pass


class TestGetAIResponse(APITestCase):
    pass


class TestGetFiveMessages(APITestCase):
    pass


class TestCalendar(APITestCase):
    pass


class TestRateDater(APITestCase):
    pass


class TestGetDaterRating(APITestCase):
    pass


class TestGetDaterAverageRating(APITestCase):
    pass


class TestDaterTransfer(APITestCase):
    pass


class TestGetDaterBalance(APITestCase):
    pass


class TestGetDaterProfile(APITestCase):
    pass


class TestSetDaterProfile(APITestCase):
    pass


class TestRateCupid(APITestCase):
    pass


class TestGetCupidRating(APITestCase):
    pass


class TestGetCupidAverageRating(APITestCase):
    pass


class TestCupidTransfer(APITestCase):
    pass


class TestGetCupidBalance(APITestCase):
    pass


class TestGetCupidProfile(APITestCase):
    pass


class TestSetCupidProfile(APITestCase):
    pass


class TestCreateGig(APITestCase):
    pass


class TestAcceptGig(APITestCase):
    pass


class TestCompleteGig(APITestCase):
    pass


class TestDropGig(APITestCase):
    pass


class TestGetGig(APITestCase):
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


class TestGetCupids(APITestCase):
    pass


class TestGetDaters(APITestCase):
    pass


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


class TestSpeechToText(APITestCase):
    pass


class TestNotify(APITestCase):
    pass


class TestUpdateUserLocation(APITestCase):
    pass
