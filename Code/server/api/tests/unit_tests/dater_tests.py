from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Code.server.api.models import *
from Code.server.api.views import *
from Code.server.api.helpers import *


class TestGetAIResponse(APITestCase):

    @patch('GPT2Tokenizer.from_pretrained')
    @patch('GPT2LMHeadModel.from_pretrained')
    def good_test(self, mock_tokenizer, mock_model):
        tokenizer = MagicMock()
        mock_tokenizer.return_value = tokenizer
        model = MagicMock()
        mock_model.return_value = model
        tokenizer.encode.return_value = [1, 2, 3]
        model.generate.return_value = [4, 5, 6]
        tokenizer.decode.return_value = "Response"
        message = "Hello"
        response = get_ai_response(message)
        assert response == "Response"
        mock_tokenizer.assert_called_once()
        mock_model.assert_called_once()
        tokenizer.encode.assert_called_once()
        model.generate.assert_called_once()
        tokenizer.decode.assert_called_once()

    @patch('GPT2Tokenizer.from_pretrained')
    @patch('GPT2LMHeadModel.from_pretrained')
    def bad_test(self, mock_tokenizer, mock_model):
        tokenizer = MagicMock()
        mock_tokenizer.return_value = tokenizer
        model = MagicMock()
        mock_model.return_value = model
        tokenizer.encode.raise_exception = Exception("Test Exception")
        message = "Hello"
        response = get_ai_response(message)
        assert response == "Test Exception"
        mock_tokenizer.assert_called_once()
        mock_model.assert_called_once()
        tokenizer.encode.assert_called_once()
        model.generate.assert_not_called()
        tokenizer.decode.assert_not_called()


class TestSendChatMessage(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/send_chat_message')
        self.view = send_chat_message

    @patch('helpers.get_location_string')
    @patch('MessageSerializer')
    @patch('helpers.get_ai_response')
    def good_test(self, mock_get_location_string, mock_message_serializer, mock_get_ai_response):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        mock_message_serializer.return_value = MagicMock()
        mock_get_ai_response.return_value = "Response"
        response = self.view(request)
        assert response.data == "Response"
        assert response.status_code == status.HTTP_200_OK
        mock_get_location_string.assert_called_once()
        mock_message_serializer.assert_called_once()
        mock_get_ai_response.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('MessageSerializer')
    @patch('helpers.get_ai_response')
    def bad_test(self, mock_get_location_string, mock_message_serializer, mock_get_ai_response):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        serializer = MagicMock()
        serializer.is_valid.return_value = False
        mock_message_serializer.return_value = serializer
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_location_string.assert_called_once()
        mock_message_serializer.assert_called_once()
        mock_get_ai_response.assert_not_called()


class TestGetMessages(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_five_messages')
        self.view = get_messages

    @patch('get_object_or_404')
    @patch('Message.objects.filter')
    @patch('MessageSerializer')
    def good_test(self, mock_get_object_or_404, mock_message_filter, mock_message_serializer):
        request = self.factory.get(self.url)
        request.user.id = 1
        pk = 1
        count = 5
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_object_or_404.return_value = MagicMock()
        mock_message_filter.return_value = ["t1", "t2", "t3", "t4", "t5"]
        mock_message_serializer.return_value = MagicMock()
        response = self.view(request, pk, count)
        assert response.status_code == status.HTTP_200_OK
        mock_get_object_or_404.assert_called_once()
        mock_message_filter.assert_called_once()
        mock_message_serializer.assert_called_once()

        request = self.factory.get(self.url)
        request.user.id = 1
        pk = 1
        count = 4
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_object_or_404.return_value = MagicMock()
        mock_message_filter.return_value = ["t1", "t2", "t3"]
        mock_message_serializer.return_value = MagicMock()
        response = self.view(request, pk, count)
        assert response.status_code == status.HTTP_200_OK
        mock_get_object_or_404.assert_called_once()
        mock_message_filter.assert_called_once()

    @patch('get_object_or_404')
    @patch('Message.objects.filter')
    @patch('MessageSerializer')
    def bad_test(self, mock_get_object_or_404, mock_message_filter, mock_message_serializer):
        request = self.factory.get(self.url)
        request.user.id = 1
        pk = 1
        count = 4
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_object_or_404.return_value = None
        response = self.view(request, pk, count)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_object_or_404.assert_called_once()
        mock_message_filter.assert_not_called()
        mock_message_serializer.assert_not_called()


class TestCalendar(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/calendar')
        self.view = calendar

    @patch('helpers.get_calendar')
    @patch('helpers.save_calendar')
    def good_test(self, mock_get_calendar, mock_save_calendar):
        request = self.factory.get(self.url)
        request.method = 'GET'
        pk = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_calendar.return_value = Response("Get Calendar", status=status.HTTP_200_OK)
        response = self.view(request, pk)
        assert response.data == "Get Calendar"
        assert response.status_code == status.HTTP_200_OK
        mock_get_calendar.assert_called_once()
        mock_save_calendar.assert_not_called()

        request = self.factory.post(self.url)
        request.method = 'POST'
        pk = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_save_calendar.return_value = Response("Save Calendar", status=status.HTTP_200_OK)
        response = self.view(request, pk)
        assert response.data == "Save Calendar"
        assert response.status_code == status.HTTP_200_OK
        mock_get_calendar.assert_not_called()
        mock_save_calendar.assert_called_once()

    @patch('helpers.get_calendar')
    @patch('helpers.save_calendar')
    def bad_test(self, mock_get_calendar, mock_save_calendar):
        request = self.factory.get(self.url)
        request.method = 'GET'
        pk = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_calendar.return_value = Response("Get Calendar", status=status.HTTP_400_BAD_REQUEST)
        response = self.view(request, pk)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_calendar.assert_called_once()
        mock_save_calendar.assert_not_called()

        request = self.factory.post(self.url)
        request.method = 'POST'
        pk = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_save_calendar.return_value = Response("Save Calendar", status=status.HTTP_400_BAD_REQUEST)
        response = self.view(request, pk)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_calendar.assert_not_called()
        mock_save_calendar.assert_called_once()


class TestGetDaterRatings(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_dater_ratings')
        self.view = get_dater_ratings

    @patch('helpers.authenticated_dater')
    @patch('get_list_or_404')
    @patch('FeedbackSerializer')
    def good_test(self, mock_authenticated_dater, mock_get_list_or_404, mock_feedback_serializer):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_authenticated_dater.return_value = MagicMock()
        mock_get_list_or_404.return_value = ["t1", "t2", "t3"]
        mock_feedback_serializer.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == ["t1", "t2", "t3"]
        mock_authenticated_dater.assert_called_once()
        mock_get_list_or_404.assert_called_once()
        mock_feedback_serializer.assert_called_once()

    @patch('helpers.authenticated_dater')
    @patch('get_list_or_404')
    @patch('FeedbackSerializer')
    def bad_test(self, mock_authenticated_dater, mock_get_list_or_404, mock_feedback_serializer):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_authenticated_dater.side_effect = PermissionDenied("Test Exception")
        response = self.view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        mock_authenticated_dater.assert_called_once()
        mock_get_list_or_404.assert_not_called()
        mock_feedback_serializer.assert_not_called()


class TestGetDaterAverageRating(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_dater_average_rating')
        self.view = get_dater_avg_rating

    @patch('helpers.authenticated_dater')
    def good_test(self, mock_authenticated_dater):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        dater = MagicMock()
        dater.rating_sum = 10
        dater.rating_count = 2
        mock_authenticated_dater.return_value = dater
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == 5.0
        mock_authenticated_dater.assert_called_once()

    @patch('helpers.authenticated_dater')
    def bad_test(self, mock_authenticated_dater):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_authenticated_dater.side_effect = PermissionDenied("Test Exception")
        response = self.view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        mock_authenticated_dater.assert_called_once()


class TestDaterTransfer(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/dater_transfer')
        self.view = dater_transfer

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    def good_test(self, mock_get_location_string, mock_get_object_or_404):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        mock_get_object_or_404.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_location_string.assert_called_once()
        mock_get_object_or_404.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    def bad_test(self, mock_get_location_string, mock_get_object_or_404):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        mock_get_object_or_404.return_value = None
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_location_string.assert_called_once()
        mock_get_object_or_404.assert_called_once()


class TestGetDaterBalance(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_dater_balance')
        self.view = get_dater_balance

    @patch('helpers.authenticated_dater')
    def good_test(self, mock_authenticated_dater):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        dater = MagicMock()
        dater.balance = 10
        mock_authenticated_dater.return_value = dater
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == 10
        mock_authenticated_dater.assert_called_once()

    @patch('helpers.authenticated_dater')
    def bad_test(self, mock_authenticated_dater):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_authenticated_dater.side_effect = PermissionDenied("Test Exception")
        response = self.view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        mock_authenticated_dater.assert_called_once()


class TestGetDaterProfile(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/get_dater_profile')
        self.view = get_dater_profile

    @patch('helpers.authenticated_dater')
    def good_test(self, mock_authenticated_dater):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        dater = MagicMock()
        dater.profile = "Profile"
        mock_authenticated_dater.return_value = dater
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == "Profile"
        mock_authenticated_dater.assert_called_once()

    @patch('helpers.authenticated_dater')
    def bad_test(self, mock_authenticated_dater):
        request = self.factory.get(self.url)
        request.user.id = 1
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_authenticated_dater.side_effect = PermissionDenied("Test Exception")
        response = self.view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        mock_authenticated_dater.assert_called_once()


class TestSetDaterProfile(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/set_dater_profile')
        self.view = set_dater_profile

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('DaterSerializer')
    @patch('UserSerializer')
    def good_test(self, mock_get_location_string, mock_get_object_or_404, mock_dater_serializer, mock_user_serializer):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        mock_get_object_or_404.return_value = MagicMock()
        mock_dater_serializer.return_value = MagicMock()
        mock_user_serializer.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_location_string.assert_called_once()
        mock_get_object_or_404.assert_called_once()
        mock_dater_serializer.assert_called_once()
        mock_user_serializer.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('DaterSerializer')
    @patch('UserSerializer')
    def bad_test(self, mock_get_location_string, mock_get_object_or_404, mock_dater_serializer, mock_user_serializer):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        mock_get_object_or_404.return_value = None
        mock_dater_serializer.return_value = MagicMock()
        mock_user_serializer.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_location_string.assert_called_once()
        mock_get_object_or_404.assert_called_once()
        mock_dater_serializer.assert_called_once()
        mock_user_serializer.assert_called_once()


class TestRateCupid(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/rate_cupid')
        self.view = rate_cupid

    @patch('helpers.update_user_location')
    @patch('Gig.objects.get')
    @patch('FeedbackSerializer')
    @patch('make_aware')
    def good_test(self, mock_update_user_location, mock_gig_get, mock_feedback_serializer, mock_make_aware):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_update_user_location.return_value = MagicMock()
        mock_gig_get.return_value = MagicMock()
        mock_feedback_serializer.return_value = MagicMock()
        mock_make_aware.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_update_user_location.assert_called_once()
        mock_gig_get.assert_called_once()
        mock_feedback_serializer.assert_called_once()
        mock_make_aware.assert_called_once()

    @patch('helpers.update_user_location')
    @patch('Gig.objects.get')
    @patch('FeedbackSerializer')
    @patch('make_aware')
    def bad_test(self, mock_update_user_location, mock_gig_get, mock_feedback_serializer, mock_make_aware):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_update_user_location.return_value = MagicMock()
        mock_gig_get.return_value = None
        mock_feedback_serializer.return_value = MagicMock()
        mock_make_aware.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_update_user_location.assert_called_once()
        mock_gig_get.assert_called_once()
        mock_feedback_serializer.assert_not_called()
        mock_make_aware.assert_not_called()


class TestCreateGig(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/create_gig')
        self.view = create_gig

    @patch('helpers.update_user_location')
    @patch('get_object_or_404')
    @patch('QuestSerializer')
    @patch('GigSerializer')
    @patch('helpers.save_serializer')
    def good_test(self, mock_update_user_location, mock_get_object_or_404, mock_quest_serializer, mock_gig_serializer,
                  mock_save_serializer):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_update_user_location.return_value = MagicMock()
        mock_get_object_or_404.return_value = MagicMock()
        mock_quest_serializer.return_value = MagicMock()
        mock_gig_serializer.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_update_user_location.assert_called_once()
        mock_get_object_or_404.assert_called_once()
        mock_quest_serializer.assert_called_once()
        mock_gig_serializer.assert_called_once()
        mock_save_serializer.assert_called_once()

    @patch('helpers.update_user_location')
    @patch('get_object_or_404')
    @patch('QuestSerializer')
    @patch('GigSerializer')
    @patch('helpers.save_serializer')
    def bad_test(self, mock_update_user_location, mock_get_object_or_404, mock_quest_serializer, mock_gig_serializer,
                 mock_save_serializer):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_update_user_location.return_value = MagicMock()
        mock_get_object_or_404.return_value = None
        mock_quest_serializer.return_value = MagicMock()
        mock_gig_serializer.return_value = MagicMock()
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_update_user_location.assert_called_once()
        mock_get_object_or_404.assert_called_once()
        mock_quest_serializer.assert_not_called()
        mock_gig_serializer.assert_not_called()
        mock_save_serializer.assert_not_called()


class TestSpeechToText(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/speech_to_text')
        self.view = speech_to_text

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('helpers.get_response_from_audio')
    @patch('helpers.process_ai_response')
    def good_test(self, mock_get_location_string, mock_get_object_or_404, mock_get_response_from_audio,
                  mock_process_ai_response):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        mock_get_object_or_404.return_value = MagicMock()
        mock_get_response_from_audio.return_value = "Response"
        mock_process_ai_response.return_value = "Processed Response"
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_location_string.assert_called_once()
        mock_get_object_or_404.assert_called_once()
        mock_get_response_from_audio.assert_called_once()
        mock_process_ai_response.assert_called_once()

    @patch('helpers.get_location_string')
    @patch('get_object_or_404')
    @patch('helpers.get_response_from_audio')
    @patch('helpers.process_ai_response')
    def bad_test(self, mock_get_location_string, mock_get_object_or_404, mock_get_response_from_audio,
                 mock_process_ai_response):
        request = self.factory.post(self.url)
        force_authenticate(request, user=User.objects.get(username='test'))
        mock_get_location_string.return_value = "Location"
        mock_get_object_or_404.return_value = None
        mock_get_response_from_audio.return_value = "Response"
        mock_process_ai_response.return_value = "Processed Response"
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        mock_get_location_string.assert_called_once()
        mock_get_object_or_404.assert_called_once()
        mock_get_response_from_audio.assert_not_called()
        mock_process_ai_response.assert_not_called()
