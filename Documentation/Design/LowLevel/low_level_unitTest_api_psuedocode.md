# Unit Tests
Each view will have a corresponding unit test. The unit tests will be used to verify that the views are functioning as expected.

- Good input will be used to verify that the views are functioning as expected
- Bad input will be used to verify that the views are functioning as expected
- Edge cases will be used to verify that the views are functioning as expected
The following tools will be used to create unit tests for the software:

- Django test framework will be used to create unit tests for the software.
    - https://docs.djangoproject.com/en/3.2/topics/testing/
- Django debug toolbar will be used to monitor the performance of the software and to identify any potential issues.
    - https://django-debug-toolbar.readthedocs.io/en/latest/

Pseudocode can be found at the bottom of the [Test pseudocode](#test-pseudocode) section.

### Test pseudocode  
api/test.api:

    from django.test import TestCase
    from unittest.mock import MagicMock

    class APITestCase(TestCase):

        def test_sign_in(self):
            mock_request = MagicMock()
            mock_request.method = "POST"
            mock_request.POST.get = MagicMock(return_value="{
                "status": "success",
                "message": "User has been signed in"
                "code": 200
            }")
            response = sign_in(mock_request)
            self.assertEqual(response.status_code, 200)
            
            mock_request.POST.get = MagicMock(return_value="{
                "status": "failure",
                "message": "Incorrect Password"
                "code": 400
            }")
            response = sign_in(mock_request)
            self.assertEqual(response.status_code, 400)
            
        def test_login(self):
            mock_request = MagicMock()
            mock_request.method = "POST"
            mock_request.POST.get = MagicMock(return_value="{
                "status": "success",
                "message": "User has been logged in"
                "code": 200
            }")
            response = login(mock_request)
            self.assertEqual(response.status_code, 200)
            
            mock_request.POST.get = MagicMock(return_value="{
                "status": "failure",
                "message": "Incorrect Password"
                "code": 400
            }")
            response = login(mock_request)
            self.assertEqual(response.status_code, 400)
            
        def test_create_user(self):
            mock_request = MagicMock()
            mock_request.method = "POST"
            mock_request.POST.get = MagicMock(return_value="{
                "status": "success",
                "message": "User has been created"
                "code": 200
            }")
            response = create_user(mock_request)
            self.assertEqual(response.status_code, 200)
            
            mock_request.POST.get = MagicMock(return_value="{
                "status": "failure",
                "message": "User has not been created"
                "code": 400
            }")
            response = create_user(mock_request)
            self.assertEqual(response.status_code, 400)
        
        # etc ...