from rest_framework.test import APIRequestFactory, force_authenticate
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from Dev._server.api.models import *
from Dev._server.api.views import *
from Dev._server.api.helpers import *


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
    def test_good(self, mock_get_location_string, mock_message_serializer, mock_get_ai_response):
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
    def test_bad(self, mock_get_location_string, mock_message_serializer, mock_get_ai_response):
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


class TestGetFiveMessages(APITestCase):
        
        def setUp(self):
            self.factory = APIRequestFactory()
            self.url = reverse('api/get_five_messages')
            self.view = get_five_messages


class TestCalendar(APITestCase):
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


class TestCreateGig(APITestCase):
    pass


class TestSpeechToText(APITestCase):
    pass
