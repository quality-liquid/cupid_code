from django.test import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
from .views import *

# good means will be tested with good input,
# bad means will be tested with bad input

class TestApi(TestCase):
    """
    Test external API calls
    """
    def test_good__get_location_string(self):
        pass

    def test_bad__get_location_string(self):
        pass

    def test_good__get_location_from_address(self):
        pass

    def test_bad__get_location_from_address(self):
        pass

    def test_good__get_location_from_ip_address(self):
        pass

    def test_bad__get_location_from_ip_address(self):
        pass

    def test_good__locations_are_near(self):
        pass

    def test_bad__locations_are_near(self):
        pass

    def test_good__haversine_distance(self):
        pass

    def test_bad__haversine_distance(self):
        pass

    def test_good__within_distance(self):
        pass

    def test_bad__within_distance(self):
        pass

    def test_good_get_stores(self):
        pass

    def test_bad_get_stores(self):
        pass

    def test_good_get_activities(self):
        pass

    def test_bad_get_activities(self):
        pass

    def test_good_get_events(self):
        pass

    def test_bad_get_events(self):
        pass

    def test_good_get_attractions(self):
        pass

    def test_bad_get_attractions(self):
        pass

    def test_good_get_restaurants(self):
        pass

    def test_bad_get_restaurants(self):
        pass

    def test_good__call_yelp_api(self):
        pass

    def test_bad__call_yelp_api(self):
        pass

    def test_good__get_yelp_api_key(self):
        pass

    def test_bad__get_yelp_api_key(self):
        pass

    def test_good_get_user_location(self):
        pass

    def test_bad_get_user_location(self):
        pass

    def test_good_speech_to_text(self):
        pass

    def test_bad_speech_to_text(self):
        pass

    def test_good_notify(self):
        pass

    def test_bad_notify(self):
        pass


class TestApiUser(TestCase):
    """
    Test general user endpoints
    """
    def test_good_create_user(self):
        pass

    def test_bad_create_user(self):
        pass

    def test_good_sign_in(self):
        pass

    def test_bad_sign_in(self):
        pass

    def test_good_sign_out(self):
        pass

    def test_bad_sign_out(self):
        pass

    def test_good_get_user(self):
        pass

    def test_bad_get_user(self):
        pass

    def test_good_delete_user(self):
        pass

    def test_bad_delete_user(self):
        pass


class TestApiDater(TestCase):
    """
    Test the dater endpoints
    """

    def test_good_send_chat_message(self):
        pass

    def test_bad_send_chat_message(self):
        pass

    def test_good__get_ai_response(self):
        pass

    def test_bad__get_ai_response(self):
        pass

    def test_good_get_five_messages(self):
        pass

    def test_bad_get_five_messages(self):
        pass

    def test_good_calendar(self):
        pass

    def test_bad_calendar(self):
        pass

    def test_good_get_dater_ratings(self):
        pass

    def test_bad_get_dater_ratings(self):
        pass

    def test_good_get_dater_avg_rating(self):
        pass

    def test_bad_get_dater_avg_rating(self):
        pass

    def test_good_dater_transfer(self):
        pass

    def test_bad_dater_transfer(self):
        pass

    def test_good_get_dater_balance(self):
        pass

    def test_bad_get_dater_balance(self):
        pass

    def test_good_get_dater_profile(self):
        pass

    def test_bad_get_dater_profile(self):
        pass

    def test_good_set_dater_profile(self):
        pass

    def test_bad_set_dater_profile(self):
        pass

    def test_good_rate_cupid(self):
        pass

    def test_bad_rate_cupid(self):
        pass


class TestApiCupid(TestCase):
    """
    Test the cupid endpoints
    """
    def test_good_rate_dater(self):
        pass

    def test_bad_rate_dater(self):
        pass

    def test_good_get_cupid_ratings(self):
        pass

    def test_bad_get_cupid_ratings(self):
        pass

    def test_good_get_cupid_avg_rating(self):
        pass

    def test_bad_get_cupid_avg_rating(self):
        pass

    def test_good_cupid_transfer(self):
        pass

    def test_bad_cupid_transfer(self):
        pass

    def test_good_get_cupid_balance(self):
        pass

    def test_bad_get_cupid_balance(self):
        pass

    def test_good_get_cupid_profile(self):
        pass

    def test_bad_get_cupid_profile(self):
        pass

    def test_good_set_cupid_profile(self):
        pass

    def test_bad_set_cupid_profile(self):
        pass

    def test_good_create_gig(self):
        pass

    def test_bad_create_gig(self):
        pass

    def test_good_accept_gig(self):
        pass

    def test_bad_accept_gig(self):
        pass

    def test_good_complete_gig(self):
        pass

    def test_bad_complete_gig(self):
        pass

    def test_good_drop_gig(self):
        pass

    def test_bad_drop_gig(self):
        pass

    def test_good_get_gigs(self):
        pass

    def test_bad_get_gigs(self):
        pass


class TestApiManager(TestCase):
    """
    Test the manager endpoints
    """
    def test_good_get_cupids(self):
        pass

    def test_bad_get_cupids(self):
        pass

    def test_good_get_daters(self):
        pass

    def test_bad_get_daters(self):
        pass

    def test_good_get_dater_count(self):
        pass

    def test_bad_get_dater_count(self):
        pass

    def test_good_get_cupid_count(self):
        pass

    def test_bad_get_cupid_count(self):
        pass

    def test_good_get_active_cupids(self):
        pass

    def test_bad_get_active_cupids(self):
        pass

    def test_good_get_active_daters(self):
        pass

    def test_bad_get_active_daters(self):
        pass

    def test_good_get_gig_rate(self):
        pass

    def test_bad_get_gig_rate(self):
        pass

    def test_good_get_gig_count(self):
        pass

    def test_bad_get_gig_count(self):
        pass

    def test_good_get_gig_drop_rate(self):
        pass

    def test_bad_get_gig_drop_rate(self):
        pass

    def test_good_get_gig_complete_rate(self):
        pass

    def test_bad_get_gig_complete_rate(self):
        pass

    def test_good_suspend(self):
        pass

    def test_bad_suspend(self):
        pass

    def test_good_unsuspend(self):
        pass

    def test_bad_unsuspend(self):
        pass
