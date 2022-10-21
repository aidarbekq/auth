from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.request_reset_password_url = reverse('request-reset-email')

        self.user_data = {
            'email': 'email@gmail.com',
            'username': 'email',
            'password': 'password',
        }
        self.user_data_for_login = {
            'email': 'email@gmail.com',
            'password': 'password',
        }
        self.user_data_for_request_reset_password = {
            'email': 'email@gmail.com'
        }
        self.user_data_for_request_reset_password_does_not_exist = {
            'email': 'email111@gmail.com'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


