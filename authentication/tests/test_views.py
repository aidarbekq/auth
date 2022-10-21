from .test_setup import TestSetup
from ..models import User


class TestViews(TestSetup):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        print(res.data)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        print(res.data)
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format='json')
        res = self.client.post(self.login_url, self.user_data_for_login, format='json')
        print(res.data)
        self.assertEqual(res.status_code, 401)

    def test_user_can_login_after_verification(self):
        register_res = self.client.post(self.register_url, self.user_data, format='json')
        print(register_res.data)
        email = register_res.data['email']
        print(email)
        user = User.objects.get(email=email)
        user.is_verified = True
        print(user)
        user.save()
        res = self.client.post(self.login_url, self.user_data_for_login, format='json')
        print(res.data)
        self.assertEqual(res.status_code, 200)

    def test_user_can_request_to_reset_password(self):
        register_res = self.client.post(self.register_url, self.user_data, format='json')
        print(register_res.data)
        email = register_res.data['email']
        print(email)
        user = User.objects.get(email=email)
        user.is_verified = True
        print(user)
        user.save()
        login_res = self.client.post(self.login_url, self.user_data_for_login, format='json')
        print(login_res.data)
        res = self.client.post(self.request_reset_password_url, self.user_data_for_request_reset_password, format='json')
        print(res.data)
        self.assertEqual(res.status_code, 200)

    def test_user_cannot_request_to_reset_password_with_email_that_does_not_exist(self):
        register_res = self.client.post(self.register_url, self.user_data, format='json')
        print(register_res.data)
        email = register_res.data['email']
        print(email)
        user = User.objects.get(email=email)
        user.is_verified = True
        print(user)
        user.save()
        login_res = self.client.post(self.login_url, self.user_data_for_login, format='json')
        print(login_res.data)
        res = self.client.post(self.request_reset_password_url, self.user_data_for_request_reset_password_does_not_exist, format='json')
        print(res.data)
        self.assertEqual(res.status_code, 400)
