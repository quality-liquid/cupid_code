from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from Code.server.api.models import User
import Code.server.api.helpers as helpers
import Code.server.api.views as views


class TestUpdateUserLocation(APITestCase):

    def good_test(self):
        user = MagicMock()
        addr = MagicMock()
        helpers.update_user_location(user, addr)
        # check that the user's location is updated
        user.save.assert_called_once()

    def bad_test(self, mock_get_location_string):
        mock_get_location_string.return_value = None
        user = MagicMock()
        addr = MagicMock()

        helpers.update_user_location(user, addr)
        # check that the user's location is not updated
        assert user.location is None
        user.save.assert_not_called()


class TestGetLocationString(APITestCase):

    def good_test(self):
        addr = MagicMock()
        s = helpers.get_location_string(addr)
        assert s == "1 2"

    def bad_test(self):
        addr = MagicMock()
        s = helpers.get_location_string(addr)
        assert s is None


class TestGetLocationFromAddress(APITestCase):

    def good_test(self):
        addr = MagicMock()
        lat, lon = helpers.get_location_from_address(addr)
        assert lat == 1
        assert lon == 2

    def bad_test(self):
        addr = MagicMock()
        lat, lon = helpers.get_location_from_address(addr)
        assert lat is None
        assert lon is None


class TestGetLocationFromIPAddress(APITestCase):

    def good_test(self):
        ip_address = MagicMock()
        lat, lon = helpers.get_location_from_ip_address(ip_address)
        assert lat == 1
        assert lon == 2

    def bad_test(self):
        ip_address = MagicMock()
        lat, lon = helpers.get_location_from_ip_address(ip_address)
        assert lat is None
        assert lon is None


class TestLocationsAreNear(APITestCase):

    def good_test(self):
        location1 = "1,2"
        location2 = "3,4"
        max_distance_miles = 5
        b = helpers.locations_are_near(location1, location2, max_distance_miles)
        assert b is True

    def bad_test(self):
        location1 = "1,2"
        location2 = "3,4"
        max_distance_miles = 5
        b = helpers.locations_are_near(location1, location2, max_distance_miles)
        assert b is False


class TestHaversineDistance(APITestCase):

    def good_test(self):
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        d = helpers.haversine_distance(lat1, lon1, lat2, lon2)
        assert d == 314.404

    def bad_test(self):
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        d = helpers.haversine_distance(lat1, lon1, lat2, lon2)
        assert d != 314.404


class TestWithinDistance(APITestCase):

    def good_test(self):
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        max_distance_miles = 5
        b = helpers.within_distance(lat1, lon1, lat2, lon2, max_distance_miles)
        assert b is True

    def bad_test(self):
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        max_distance_miles = 5
        b = helpers.within_distance(lat1, lon1, lat2, lon2, max_distance_miles)
        assert b is False


class TestRequestYelpAPI(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.urls = ['get_stores', 'get_activities', 'get_events', 'get_restaurants', 'get_attractions']
        self.views = [views.get_stores, views.get_activities, views.get_events, views.get_restaurants, views.get_attractions]

    def good_test(self):
        for url, view in zip(self.urls, self.views):
            request = self.factory.get(reverse(url))
            force_authenticate(request, user=User.objects.create())
            response = view(request)
            assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        for url, view in zip(self.urls, self.views):
            request = self.factory.get(reverse(url))
            force_authenticate(request, user=User.objects.create())
            response = view(request)
            assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestGetResponseFromYelpAPI(APITestCase):
    def good_test(self):
        pk = 1
        request = MagicMock()
        search = MagicMock()
        response = helpers.get_response_from_yelp_api(pk, request, search)
        assert response.status_code == status.HTTP_200_OK

    def bad_test(self):
        pk = 1
        request = MagicMock()
        search = MagicMock()
        response = helpers.get_response_from_yelp_api(pk, request, search)
        assert response is None
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestCallYelpAPI(APITestCase):
    @patch("get_object_or_404")
    @patch("YelpAPI")
    def good_test(self, mock_get_object_or_404, mock_YelpAPI):
        mock_get_object_or_404.return_value = MagicMock()
        mock_YelpAPI.return_value = MagicMock()
        pk = 1
        search = MagicMock()
        data = helpers.call_yelp_api(pk, search)
        assert data is not None
        mock_get_object_or_404.assert_called_once()
        mock_YelpAPI.assert_called_once()

    @patch("get_object_or_404")
    @patch("YelpAPI")
    def bad_test(self, mock_get_object_or_404, mock_YelpAPI):
        mock_get_object_or_404.return_value = None
        mock_YelpAPI.return_value = MagicMock()
        pk = 1
        search = MagicMock()
        data = helpers.call_yelp_api(pk, search)
        assert data is None
        mock_get_object_or_404.assert_called_once()
        mock_YelpAPI.assert_called_once()


class TestNotify(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.urls = "api/notify"
        self.views = views.notify

    @patch("get_object_or_404")
    def good_test(self, mock_get_object_or_404):
        dater = MagicMock()
        dater.communication_preference = 0
        mock_get_object_or_404.return_value = dater
        request = self.factory.get(reverse(self.urls))
        force_authenticate(request, user=User.objects.create())

        # Test 1: Email
        response = self.views(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_object_or_404.assert_called_once()

        # Test 2: Text
        dater.communication_preference = 1
        response = self.views(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_object_or_404.assert_called_once()

    @patch("get_object_or_404")
    def bad_test(self, mock_get_object_or_404):
        mock_get_object_or_404.return_value = None
        request = self.factory.get(reverse(self.urls))
        force_authenticate(request, user=User.objects.create())
        response = self.views(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_object_or_404.assert_called_once()


class TestCreateNewGig(APITestCase):
    @patch("QuestSerializer")
    @patch("GigSerializer")
    def good_test(self, mock_quest_serializer, mock_gig_serializer):
        dater = MagicMock()
        dater.budget = 1
        ai_response = """
        Create gig: True
        Items requested: Flowers
        """
        mock_locations = [{
            'address': 'test address'
        }]
        mock_quest_serializer.return_value = MagicMock()
        mock_gig_serializer.return_value = MagicMock()

        response = helpers.create_new_gig(dater, ai_response)
        assert response.status_code == status.HTTP_200_OK
        mock_quest_serializer.assert_called_once()
        mock_gig_serializer.assert_called_once()
        assert response.data['message'] == 'gig was created'

    @patch("call_yelp_api")
    @patch("QuestSerializer")
    @patch("GigSerializer")
    def bad_test(self, mock_yelp_api, mock_quest_serializer, mock_gig_serializer):
        dater = MagicMock()
        request = None
        mock_yelp_api.return_value = MagicMock()
        mock_quest_serializer.return_value = MagicMock()
        mock_gig_serializer.return_value = MagicMock()

        response = helpers.create_new_gig(dater, request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_yelp_api.assert_called_once()
        mock_quest_serializer.assert_called_once()
        mock_gig_serializer.assert_called_once()


class TestSendEmail(APITestCase):
    @patch("Mail")
    @patch("get_grid_api_key")
    @patch("SendGridAPIClient")
    def good_test(self, mock_mail, mock_get_grid_api_key, mock_send_grid):
        dater = MagicMock()
        message = "Test"
        dater.email = "Dater email"
        mock_mail.return_value = MagicMock()
        mock_get_grid_api_key.return_value = "key"
        mock_send_grid.return_value = MagicMock()

        response = helpers.send_email(dater, message)
        assert response.status_code == status.HTTP_200_OK
        mock_mail.assert_called_once()
        mock_get_grid_api_key.assert_called_once()
        mock_send_grid.assert_called_once()

    @patch("Mail")
    @patch("get_grid_api_key")
    @patch("SendGridAPIClient")
    def bad_test(self, mock_mail, mock_get_grid_api_key, mock_send_grid):
        dater = MagicMock()
        message = "Test"
        dater.email = None
        mock_mail.return_value = MagicMock()
        mock_get_grid_api_key.return_value = "key"
        mock_send_grid.return_value = MagicMock()

        response = helpers.send_email(dater, message)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_mail.assert_called_once()
        mock_get_grid_api_key.assert_called_once()
        mock_send_grid.assert_called_once()


class TestSendText(APITestCase):
    @patch("get_twilio_authenticated_reserve_phone_number")
    @patch("get_twilio_authenticated_sender_phone_number")
    @patch("Client")
    @patch("Client.messages.create")
    def good_test(self, mock_reserve_number, mock_sender_number, mock_client, mock_message_create):
        account_sid = "sid"
        auth_token = "token"
        message = "Test"
        mock_reserve_number.return_value = "1234567890"
        mock_sender_number.return_value = "0987654321"
        mock_client.return_value = MagicMock()
        mock_message_create.return_value = MagicMock()

        response = helpers.send_text(account_sid, auth_token, message)
        assert response.status_code == status.HTTP_200_OK
        mock_reserve_number.assert_called_once()
        mock_sender_number.assert_called_once()
        mock_client.assert_called_once()
        mock_message_create.assert_called_once()

    @patch("get_twilio_authenticated_reserve_phone_number")
    @patch("get_twilio_authenticated_sender_phone_number")
    @patch("Client")
    @patch("Client.messages.create")
    def bad_test(self, mock_reserve_number, mock_sender_number, mock_client, mock_message_create):
        account_sid = "sid"
        auth_token = None
        message = "Test"
        mock_reserve_number.return_value = "1234567890"
        mock_sender_number.return_value = "0987654321"
        mock_client.return_value = MagicMock()
        mock_message_create.return_value = MagicMock()

        response = helpers.send_text(account_sid, auth_token, message)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_reserve_number.assert_called_once()
        mock_sender_number.assert_called_once()
        mock_client.assert_called_once()
        mock_message_create.assert_not_called()


class TestGetResponseFromAudio(APITestCase):

    def good_test(self):
        audio_data = "audio data test"
        audio_type = "audio type test"
        dater = MagicMock()

        response = helpers.get_response_from_audio(audio_data, audio_type, dater)
        assert response.status_code == status.HTTP_200_OK


    def bad_test(self):
        # Testing with no audio data
        audio_data = None
        audio_type = "audio type test"
        dater = MagicMock()

        response = helpers.get_response_from_audio(audio_data, audio_type, dater)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
