from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from api.views import *


class TestRateDater(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/rate_dater')
        self.view = rate_dater
        self.user = MagicMock()

    @patch('helpers.update_location')
    @patch('Gig.objects.get')
    @patch('FeedbackSerializer')
    def test_good_test(self, mock_update_location, mock_get, mock_serializer):
        mock_update_location.return_value = None
        mock = MagicMock()
        mock.dater.id = 1
        mock_get.return_value = mock
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        force_authenticate(request, user=self.user)
        request.data = {'gig_id': 1, 'rating': 5, 'message': 'test', 'dater_id': 1}
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_update_location.assert_called_once()
        mock_get.assert_called_once()
        mock_serializer.assert_called_once()

    @patch('helpers.update_location')
    @patch('Gig.objects.get')
    @patch('FeedbackSerializer')
    def test_bad_test(self, mock_update_location, mock_get, mock_serializer):
        mock_update_location.return_value = None
        mock = MagicMock()
        mock.dater.id = 2
        mock_get.return_value = mock
        mock_serializer.return_value = MagicMock()
        request = self.factory.post(self.url)
        force_authenticate(request, user=self.user)
        request.data = {'gig_id': 1, 'rating': 5, 'message': 'test', 'dater_id': 1}
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        mock_update_location.assert_called_once()
        mock_get.assert_called_once()
        mock_serializer.assert_not_called()

class TestGetCupidRating(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_cupid_ratings')
        self.view = get_cupid_ratings
        self.user = MagicMock()

    @patch('get_list_or_404')
    @patch('FeedbackSerializer')
    def test_good_test(self, mock_get_list, mock_serializer):
        mock_get_list.return_value = []
        mock_serializer.return_value = MagicMock()
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_get_list.assert_called_once()
        mock_serializer.assert_called_once()

    @patch('get_list_or_404')
    @patch('FeedbackSerializer')
    def test_bad_test(self, mock_get_list, mock_serializer):
        mock_get_list.return_value = []
        mock_serializer.return_value = MagicMock()
        request = self.factory.get(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_get_list.assert_called_once()
        mock_serializer.assert_not_called()


class TestGetCupidAverageRating(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_cupid_avg_rating')
        self.view = get_cupid_avg_rating
        self.user = MagicMock()

    @patch('helpers.authenticated_cupid')
    def test_good_test(self, mock_auth):
        mock_auth.return_value = self.user
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_auth.assert_called_once()

    @patch('helpers.authenticated_cupid')
    def test_bad_test(self, mock_auth):
        mock_auth.return_value = None
        request = self.factory.get(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_auth.assert_called_once()


class TestCupidTransfer(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/cupid_transfer')
        self.view = cupid_transfer

    @patch('helpers.update_user_location')
    @patch('get_object_or_404')
    def test_good_test(self, mock_update_location, mock_get):
        mock_update_location.return_value = None
        mock_get.return_value = MagicMock()
        request = self.factory.post(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_update_location.assert_called_once()
        mock_get.assert_called_once()

    @patch('helpers.update_user_location')
    @patch('get_object_or_404')
    def test_bad_test(self, mock_update_location, mock_get):
        mock_update_location.return_value = None
        mock_get.return_value = None
        request = self.factory.post(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_update_location.assert_not_called()
        mock_get.assert_not_called()


class TestSaveBankAccount(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/save_bank_account')
        self.view = save_bank_account

    @patch('helpers.update_user_location')
    @patch('BankAccountSerializer')
    @patch('helpers.changed_response')
    def test_good_test(self, mock_update_location, mock_serializer, mock_response):
        mock_update_location.return_value = None
        mock_serializer.return_value = MagicMock()
        mock_response.return_value = Response(status=status.HTTP_200_OK)
        request = self.factory.post(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_update_location.assert_called_once()
        mock_serializer.assert_called_once()
        mock_response.assert_called_once()

    @patch('helpers.update_user_location')
    @patch('BankAccountSerializer')
    @patch('helpers.changed_response')
    def test_bad_test(self, mock_update_location, mock_serializer, mock_response):
        mock_update_location.return_value = None
        mock_serializer.return_value = MagicMock()
        mock_response.return_value = Response(status=status.HTTP_404_NOT_FOUND)
        request = self.factory.post(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_update_location.assert_not_called()
        mock_serializer.assert_not_called()
        mock_response.assert_not_called()


class TestGetCupidBalance(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_cupid_balance')
        self.view = get_cupid_balance

    @patch('helpers.authenticated_cupid')
    def test_good_test(self, mock_auth):
        cupid = MagicMock()
        cupid.balance = 0
        mock_auth.return_value = cupid
        request = self.factory.get(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_auth.assert_called_once()
        assert response.data['balance'] == 0

    @patch('helpers.authenticated_cupid')
    def test_bad_test(self, mock_auth):
        mock_auth.return_value = None
        request = self.factory.get(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_auth.assert_called_once()


class TestGetCupidProfile(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_cupid_profile')
        self.view = get_cupid_profile

    @patch('helpers.authenticated_cupid')
    @patch('CupidSerializer')
    def test_good_test(self, mock_auth, mock_serializer):
        cupid = MagicMock()
        mock_auth.return_value = cupid
        mock_serializer.return_value = MagicMock()
        request = self.factory.get(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_auth.assert_called_once()
        mock_serializer.assert_called_once()

    @patch('helpers.authenticated_cupid')
    @patch('CupidSerializer')
    def test_bad_test(self, mock_auth, mock_serializer):
        mock_auth.return_value = None
        mock_serializer.return_value = MagicMock()
        request = self.factory.get(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_auth.assert_called_once()
        mock_serializer.assert_not_called()


class TestSetCupidProfile(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/set_cupid_profile')
        self.view = set_cupid_profile

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('CupidSerializer')
    @patch('UserSerializer')
    def test_good_test(self, mock_location, mock_get, mock_cupid, mock_user):
        mock_location.return_value = 'test'
        mock_get.return_value = MagicMock()
        mock_cupid.return_value = MagicMock()
        mock_user.return_value = MagicMock()
        request = self.factory.post(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_cupid.assert_called_once()
        mock_user.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('CupidSerializer')
    @patch('UserSerializer')
    def test_bad_test(self, mock_location, mock_get, mock_cupid, mock_user):
        mock_location.return_value = 'test'
        mock_get.return_value = None
        mock_cupid.return_value = MagicMock()
        mock_user.return_value = MagicMock()
        request = self.factory.post(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_cupid.assert_not_called()
        mock_user.assert_not_called()



class TestAcceptGig(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/accept_gig')
        self.view = accept_gig

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('GigSerializer')
    @patch('make_aware')
    @patch('helpers.retrieved_response')
    def test_good_test(self, mock_location, mock_get, mock_gig, mock_make_aware, mock_response):
        mock_location.return_value = 'test'
        mock_get.return_value = MagicMock()
        mock_gig.return_value = MagicMock()
        mock_make_aware.return_value = None
        mock_response.return_value = Response(status=status.HTTP_200_OK)
        request = self.factory.post(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_gig.assert_called_once()
        mock_make_aware.assert_called_once()
        mock_response.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('GigSerializer')
    @patch('make_aware')
    @patch('helpers.retrieved_response')
    def test_bad_test(self, mock_location, mock_get, mock_gig, mock_make_aware, mock_response):
        mock_location.return_value = 'test'
        mock_get.return_value = None
        mock_gig.return_value = MagicMock()
        mock_make_aware.return_value = None
        mock_response.return_value = Response(status=status.HTTP_404_NOT_FOUND)
        request = self.factory.post(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_gig.assert_not_called()
        mock_make_aware.assert_not_called()
        mock_response.assert_not_called()


class TestCompleteGig(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/complete_gig')
        self.view = complete_gig

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('GigSerializer')
    @patch('make_aware')
    @patch('helpers.changed_response')
    def test_good_test(self, mock_location, mock_get, mock_gig, mock_make_aware, mock_response):
        mock_location.return_value = 'test'
        mock_get.return_value = MagicMock()
        mock_gig.return_value = MagicMock()
        mock_make_aware.return_value = None
        mock_response.return_value = Response(status=status.HTTP_200_OK)
        request = self.factory.post(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_gig.assert_called_once()
        mock_make_aware.assert_called_once()
        mock_response.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('GigSerializer')
    @patch('make_aware')
    @patch('helpers.changed_response')
    def test_bad_test(self, mock_location, mock_get, mock_gig, mock_make_aware, mock_response):
        mock_location.return_value = 'test'
        mock_get.return_value = None
        mock_gig.return_value = MagicMock()
        mock_make_aware.return_value = None
        mock_response.return_value = Response(status=status.HTTP_404_NOT_FOUND)
        request = self.factory.post(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_gig.assert_not_called()
        mock_make_aware.assert_not_called()
        mock_response.assert_not_called()


class TestDropGig(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/drop_gig')
        self.view = drop_gig

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('GigSerializer')
    @patch('helpers.retrieved_response')
    def test_good_test(self, mock_location, mock_get, mock_gig, mock_response):
        mock_location.return_value = 'test'
        mock_get.return_value = MagicMock()
        mock_gig.return_value = MagicMock()
        mock_response.return_value = Response(status=status.HTTP_200_OK)
        request = self.factory.post(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_gig.assert_called_once()
        mock_response.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('GigSerializer')
    @patch('helpers.retrieved_response')
    def test_bad_test(self, mock_location, mock_get, mock_gig, mock_response):
        mock_location.return_value = 'test'
        mock_get.return_value = None
        mock_gig.return_value = MagicMock()
        mock_response.return_value = Response(status=status.HTTP_404_NOT_FOUND)
        request = self.factory.post(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_location.assert_called_once()
        mock_get.assert_called_once()
        mock_gig.assert_not_called()
        mock_response.assert_not_called()


class TestGetGig(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_gig')
        self.view = get_gigs

    @patch('get_object_or_404')
    @patch('helpers.update_user_location')
    @patch('Gig.objects.all')
    @patch('helpers.locations_are_near')
    @patch('GigSerializer')
    def test_good_test(self, mock_get, mock_update, mock_all, mock_near, mock_serializer):
        mock_get.return_value = MagicMock()
        mock_update.return_value = None
        mock_all.return_value = []
        mock_near.return_value = True
        mock_serializer.return_value = MagicMock()
        request = self.factory.get(self.url)
        force_authenticate(request, user=MagicMock())
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_get.assert_called_once()
        mock_update.assert_called_once()
        mock_all.assert_called_once()
        mock_near.assert_called_once()
        mock_serializer.assert_called_once()

    @patch('get_object_or_404')
    @patch('helpers.update_user_location')
    @patch('Gig.objects.all')
    @patch('helpers.locations_are_near')
    @patch('GigSerializer')
    def test_bad_test(self, mock_get, mock_update, mock_all, mock_near, mock_serializer):
        mock_get.return_value = MagicMock()
        mock_update.return_value = None
        mock_all.return_value = []
        mock_near.return_value = False
        mock_serializer.return_value = MagicMock()
        request = self.factory.get(self.url)
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        mock_get.assert_called_once()
        mock_update.assert_called_once()
        mock_all.assert_called_once()
        mock_near.assert_called_once()
        mock_serializer.assert_not_called()
