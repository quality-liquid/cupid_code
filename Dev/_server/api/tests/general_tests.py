from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
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


class TestNotify(APITestCase):
    pass
