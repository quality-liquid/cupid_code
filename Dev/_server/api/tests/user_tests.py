from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from Dev._server.api.views import *


class TestCreateUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/create_user')
        self.view = create_user

    @patch("UserSerializer")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch('helpers.update_location')
    def good_test(self, mock_user, mock_dater, mock_cupid, mock_update_location):
        mock_user.return_value = MagicMock()
        mock_dater.return_value = MagicMock()
        mock_cupid.return_value = MagicMock()
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'user_id': 1, 'location': 'Test', 'role': 'dater', 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_201_CREATED
        mock_user.assert_called_once()
        mock_dater.assert_called_once()
        mock_cupid.assert_not_called()

    @patch("UserSerializer")
    @patch("DaterSerializer")
    @patch("CupidSerializer")
    @patch('helpers.update_location')
    def bad_test(self, mock_user, mock_dater, mock_cupid, mock_update_location):
        mock_user.return_value = MagicMock()
        mock_dater.return_value = MagicMock()
        mock_cupid.return_value = MagicMock()
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        
        request.data = {'user_id': 1, 'location': 'Test', 'role': None, 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['error'] == 'invalid user type'
        mock_user.assert_called_once()
        mock_dater.assert_not_called()
        mock_cupid.assert_not_called()


class TestSignIn(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api/sign_in')
        self.view = sign_in
        self.user = MagicMock()

    @patch('User.objects.get')
    @patch('helpers.update_location')
    def good_test(self, mock_get_user, mock_update_location):
        mock = MagicMock()
        # TODO Pretty sure I need to tie in 'username' somehow. Test that an incorrect username yields bad login
        mock.user_id = 1
        mock_get_user.return_value = mock
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        force_authenticate(request, user=self.user)

        request.data = {'user_id': 1, 'location': 'Test', 'role': 'dater', 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_user.assert_called_once()
        mock_update_location.assert_called_once()

    @patch('User.objects.get')
    @patch('helpers.update_location')
    def bad_test(self, mock_get_user, mock_update_location):
        mock = MagicMock()
        mock.user_id = 1
        mock_get_user.return_value = mock
        mock_update_location.return_value = None
        request = self.factory.post(self.url)
        force_authenticate(request, user=self.user)

        request.data = {'user_id': 1, 'location': 'Test', 'role': 'dater', 'phone_number': '1123456789'}
        response = self.view(request)
        assert response.status_code == status.HTTP_200_OK
        mock_get_user.assert_called_once()
        mock_update_location.assert_called_once()
        




class TestGetUser(APITestCase):
    pass


class TestUserExpand(APITestCase):
    pass


class TestDeleteUser(APITestCase):
    pass
