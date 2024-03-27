from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework.test import APITestCase
from Dev._server.api.views import *
from Dev._server.api.helpers import *


class TestUpdateUserLocation(APITestCase):

    @patch("get_location_string")
    def good_test(self, mock_get_location_string):
        mock_get_location_string.return_value = MagicMock()
        user = MagicMock()
        addr = MagicMock()
        update_user_location(user, addr)
        # check that get_location_string is called
        mock_get_location_string.assert_called_once()
        # check that the user's location is updated
        assert user.location == mock_get_location_string.return_value
        user.save.assert_called_once()

    @patch("get_location_string")
    def bad_test(self, mock_get_location_string):
        mock_get_location_string.return_value = None
        user = MagicMock()
        addr = MagicMock()

        update_user_location(user, addr)
        # check that the user's location is not updated
        assert user.location is None
        user.save.assert_not_called()


class TestGetLocationString(APITestCase):

    @patch("get_location_from_ip_address")
    def good_test(self, mock_get_location_from_ip_address):
        mock_get_location_from_ip_address.return_value = (1, 2)
        addr = MagicMock()
        s = get_location_string(addr)
        assert s == "1 2"
        mock_get_location_from_ip_address.assert_called_once()

    @patch("get_location_from_ip_address")
    def bad_test(self, mock_get_location_from_ip_address):
        mock_get_location_from_ip_address.return_value = (None, None)
        addr = MagicMock()
        s = get_location_string(addr)
        assert s is None
        mock_get_location_from_ip_address.assert_called_once()


class TestGetLocationFromAddress(APITestCase):

    @patch("geopy.geocoders.Nominatim")
    @patch("geopy.geocoders.Nominatim.geocode")
    def good_test(self, mock_nominatim, mock_geocode):
        mock_nominatim.return_value = MagicMock()
        mock_geocode.return_value = MagicMock(latitude=1, longitude=2)
        addr = MagicMock()
        lat, lon = get_location_from_address(addr)
        assert lat == 1
        assert lon == 2
        mock_nominatim.assert_called_once()
        mock_geocode.assert_called_once()

    @patch("geopy.geocoders.Nominatim")
    @patch("geopy.geocoders.Nominatim.geocode")
    def bad_test(self, mock_nominatim, mock_geocode):
        mock_nominatim.return_value = MagicMock()
        mock_geocode.return_value = None
        addr = MagicMock()
        lat, lon = get_location_from_address(addr)
        assert lat is None
        assert lon is None
        mock_nominatim.assert_called_once()
        mock_geocode.assert_called_once()


class TestGetLocationFromIPAddress(APITestCase):

    @patch("geoip2.database.Reader")
    def good_test(self, mock_reader):
        mock_reader.return_value = MagicMock()
        mock_reader.city.return_value = MagicMock(location=MagicMock(latitude=1, longitude=2))
        ip_address = MagicMock()
        lat, lon = get_location_from_ip_address(ip_address)
        assert lat == 1
        assert lon == 2
        mock_reader.assert_called_once()
        mock_reader.city.assert_called_once()

    @patch("geoip2.database.Reader")
    def bad_test(self, mock_reader):
        mock_reader.return_value = MagicMock()
        mock_reader.city.side_effect = geoip2.errors.AddressNotFoundError
        ip_address = MagicMock()
        lat, lon = get_location_from_ip_address(ip_address)
        assert lat is None
        assert lon is None
        mock_reader.assert_called_once()
        mock_reader.city.assert_called_once()


class TestLocationsAreNear(APITestCase):

    @patch("within_distance")
    def good_test(self, mock_within_distance):
        mock_within_distance.return_value = True
        location1 = "1,2"
        location2 = "3,4"
        max_distance_miles = 5
        b = locations_are_near(location1, location2, max_distance_miles)
        assert b is True
        mock_within_distance.assert_called_once()

    @patch("within_distance")
    def bad_test(self, mock_within_distance):
        mock_within_distance.return_value = False
        location1 = "1,2"
        location2 = "3,4"
        max_distance_miles = 5
        b = locations_are_near(location1, location2, max_distance_miles)
        assert b is False
        mock_within_distance.assert_called_once()


class TestHaversineDistance(APITestCase):

    def good_test(self):
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        d = haversine_distance(lat1, lon1, lat2, lon2)
        assert d == 314.404

    def bad_test(self):
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        d = haversine_distance(lat1, lon1, lat2, lon2)
        assert d != 314.404


class TestWithinDistance(APITestCase):

    @patch("haversine_distance")
    def good_test(self, mock_haversine_distance):
        mock_haversine_distance.return_value = 5
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        max_distance_miles = 5
        b = within_distance(lat1, lon1, lat2, lon2, max_distance_miles)
        assert b is True

    @patch("haversine_distance")
    def bad_test(self, mock_haversine_distance):
        mock_haversine_distance.return_value = 6
        lat1 = 1
        lon1 = 2
        lat2 = 3
        lon2 = 4
        max_distance_miles = 5
        b = within_distance(lat1, lon1, lat2, lon2, max_distance_miles)
        assert b is False


class TestRequestYelpAPI(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.urls = ['get_stores', 'get_activities', 'get_events', 'get_restaurants', 'get_attractions']
        self.views = [get_stores, get_activities, get_events, get_restaurants, get_attractions]

    @patch("helpers.get_response_from_yelp_api")
    def good_test(self, mock_get_response_from_yelp_api):
        for url, view in zip(self.urls, self.views):
            mock_get_response_from_yelp_api.return_value = MagicMock()
            request = self.factory.get(reverse(url))
            force_authenticate(request, user=User.objects.create())
            response = view(request)
            assert response.status_code == status.HTTP_200_OK
            mock_get_response_from_yelp_api.assert_called_once()

    @patch("helpers.get_response_from_yelp_api")
    def bad_test(self, mock_get_response_from_yelp_api):
        for url, view in zip(self.urls, self.views):
            mock_get_response_from_yelp_api.return_value = None
            request = self.factory.get(reverse(url))
            force_authenticate(request, user=User.objects.create())
            response = view(request)
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            mock_get_response_from_yelp_api.assert_called_once()


class TestGetResponseFromYelpAPI(APITestCase):
    @patch("call_yelp_api")
    def good_test(self, mock_call_yelp_api):
        mock_call_yelp_api.return_value = MagicMock()
        pk = 1
        request = MagicMock()
        search = MagicMock()
        response = get_response_from_yelp_api(pk, request, search)
        assert response == mock_call_yelp_api.return_value
        mock_call_yelp_api.assert_called_once()
        assert response.status_code == status.HTTP_200_OK

    @patch("call_yelp_api")
    def bad_test(self, mock_call_yelp_api):
        mock_call_yelp_api.return_value = None
        pk = 1
        request = MagicMock()
        search = MagicMock()
        response = get_response_from_yelp_api(pk, request, search)
        assert response is None
        mock_call_yelp_api.assert_called_once()
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestCallYelpAPI(APITestCase):
    @patch("get_object_or_404")
    @patch("get_yelp_api_key")
    @patch("YelpAPI")
    def good_test(self, mock_get_object_or_404, mock_get_yelp_api_key, mock_YelpAPI):
        mock_get_object_or_404.return_value = MagicMock()
        mock_get_yelp_api_key.return_value = "key"
        mock_YelpAPI.return_value = MagicMock()
        pk = 1
        search = MagicMock()
        data = call_yelp_api(pk, search)
        assert data is not None
        mock_get_object_or_404.assert_called_once()
        mock_get_yelp_api_key.assert_called_once()
        mock_YelpAPI.assert_called_once()

    @patch("get_object_or_404")
    @patch("get_yelp_api_key")
    @patch("YelpAPI")
    def bad_test(self, mock_get_object_or_404, mock_get_yelp_api_key, mock_YelpAPI):
        mock_get_object_or_404.return_value = None
        mock_get_yelp_api_key.return_value = "key"
        mock_YelpAPI.return_value = MagicMock()
        pk = 1
        search = MagicMock()
        data = call_yelp_api(pk, search)
        assert data is None
        mock_get_object_or_404.assert_called_once()
        mock_get_yelp_api_key.assert_called_once()
        mock_YelpAPI.assert_called_once()


class TestNotify(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.urls = "api/notify"
        self.views = notify

    @patch("send_email")
    @patch("send_text")
    @patch("get_object_or_404")
    def good_test(self, mock_send_email, mock_send_text, mock_get_object_or_404):
        dater = MagicMock()
        dater.communication_preference = 0
        mock_get_object_or_404.return_value = dater
        mock_send_email.return_value = MagicMock()
        mock_send_text.return_value = MagicMock()
        request = self.factory.get(reverse(self.urls))
        force_authenticate(request, user=User.objects.create())

        # Test 1: Email
        response = self.views(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_object_or_404.assert_called_once()
        mock_send_email.assert_called_once()

        # Test 2: Text
        dater.communication_preference = 1
        response = self.views(request)
        assert response.statuc_code == status.HTTP_200_OK
        mock_get_object_or_404.assert_called_once()
        mock_send_text.assert_called_once()

    @patch("send_email")
    @patch("send_text")
    @patch("get_object_or_404")
    def bad_test(self, mock_send_email, mock_send_text, mock_get_object_or_404):
        mock_get_object_or_404.return_value = None
        mock_send_email.return_value = MagicMock()
        mock_send_text.return_value = MagicMock()
        request = self.factory.get(reverse(self.urls))
        force_authenticate(request, user=User.objects.create())
        response = self.views(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_object_or_404.assert_called_once()
        mock_send_email.assert_not_called()
        mock_send_text.assert_not_called()


class TestCreateNewGig(APITestCase):
    @patch("call_yelp_api")
    @patch("QuestSerializer")
    @patch("GigSerializer")
    def good_test(self, mock_yelp_api, mock_quest_serializer, mock_gig_serializer):
        dater = MagicMock()
        dater.budget = 1
        ai_response = """
        Create gig: True
        Items requested: Flowers
        """
        mock_locations = [{
            'address' : 'test address'
        }]
        mock_yelp_api.return_value = mock_locations
        mock_quest_serializer.return_value = MagicMock()
        mock_gig_serializer.return_value = MagicMock()

        response = create_new_gig(dater, ai_response)
        assert response.status_code == status.HTTP_200_OK
        mock_yelp_api.assert_called_once()
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

        response = create_new_gig(dater, request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_yelp_api.assert_called_once()
        mock_quest_serializer.assert_called_once()
        mock_gig_serializer.assert_called_once()

                   
class TestSendEmail(APITestCase):
    @patch("get_twilio_authenticated_sender_email")
    @patch("Mail")
    @patch("get_grid_api_key")
    @patch("SendGridAPIClient")
    def good_test(self, mock_get_twilio, mock_mail, mock_get_grid_api_key, mock_send_grid):
        dater = MagicMock()
        message = "Test"
        dater.email = "Dater email"
        mock_get_twilio.return_value = "from email"
        mock_mail.return_value = MagicMock()
        mock_get_grid_api_key.return_value = "key"
        mock_send_grid.return_value = MagicMock()

        response = send_email(dater, message)
        assert response.status_code == status.HTTP_200_OK
        mock_get_twilio.assert_called_once()
        mock_mail.assert_called_once()
        mock_get_grid_api_key.assert_called_once()
        mock_send_grid.assert_called_once()

    @patch("get_twilio_authenticated_sender_email")
    @patch("Mail")
    @patch("get_grid_api_key")
    @patch("SendGridAPIClient")
    def bad_test(self, mock_get_twilio, mock_mail, mock_get_grid_api_key, mock_send_grid):
        dater = MagicMock()
        message = "Test"
        dater.email = None
        mock_get_twilio.return_value = "from email"
        mock_mail.return_value = MagicMock()
        mock_get_grid_api_key.return_value = "key"
        mock_send_grid.return_value = MagicMock()       

        response = send_email(dater, message)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_twilio.assert_called_once()
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

        response = send_text(account_sid, auth_token, message)
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

        response = send_text(account_sid, auth_token, message)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_reserve_number.assert_called_once()
        mock_sender_number.assert_called_once()
        mock_client.assert_called_once()
        mock_message_create.assert_not_called()


class TestGetResponseFromAudio(APITestCase):
    @patch("speech_recognition.Recognizer")
    @patch("base64.b64decode")
    @patch("open")
    @patch("speech_recognition.AudioFile")
    @patch("recognizer.record")
    @patch("recognizer.recognize_sphinx")
    @patch("get_ai_response")
    def good_test(self, mock_recognizer, mock_base64, mock_open, mock_audiofile, mock_record, mock_recognize_sphinx, mock_ai_response)
        audio_data = "audio data test"
        audio_type = "audio type test"
        dater = MagicMock()
        mock_recognizer.return_value = MagicMock()
        mock_base64.return_value = MagicMock()
        mock_open.return_value = MagicMock()
        mock_audiofile.return_value = MagicMock()
        mock_record.return_value = MagicMock()
        mock_recognize_sphinx.return_value = MagicMock()
        mock_ai_response.return_value = MagicMock()

        response = get_response_from_audio(audio_data, audio_type, dater)
        assert response.status_code == status.HTTP_200_OK
        mock_recognizer.assert_called_once()
        mock_base64.assert_called_once()
        mock_open.assert_called_once()
        mock_audiofile.assert_called_once()
        mock_record.assert_called_once()
        mock_recognize_sphinx.assert_called_once()
        mock_ai_response.assert_called_once()

    @patch("speech_recognition.Recognizer")
    @patch("base64.b64decode")
    @patch("open")
    @patch("speech_recognition.AudioFile")
    @patch("recognizer.record")
    @patch("recognizer.recognize_sphinx")
    @patch("get_ai_response")
    def bad_test(self, mock_recognizer, mock_base64, mock_open, mock_audiofile, mock_record, mock_recognize_sphinx, mock_ai_response)
        # Testing with no audio data
        audio_data = None
        audio_type = "audio type test"
        dater = MagicMock()
        mock_recognizer.return_value = MagicMock()
        mock_base64.return_value = MagicMock()
        mock_open.return_value = MagicMock()
        mock_audiofile.return_value = MagicMock()
        mock_record.return_value = MagicMock()
        mock_recognize_sphinx.return_value = MagicMock()
        mock_ai_response.return_value = MagicMock()

        response = get_response_from_audio(audio_data, audio_type, dater)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_recognizer.assert_called_once()
        mock_base64.assert_called_once()
        # With no audio data, rest shouldn't be called, right?
        mock_open.assert_not_called()
        mock_audiofile.assert_not_called()
        mock_record.assert_not_called()
        mock_recognize_sphinx.assert_not_called()
        mock_ai_response.assert_not_called()
    
