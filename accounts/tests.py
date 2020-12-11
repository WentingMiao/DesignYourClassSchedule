
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .views import *
class loginTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='miao', email='miao@gmail', password='password')


    def test_login_anoymousUser(self):
      request = self.factory.get("/accounts/login")
      request.user = AnonymousUser()
      response = account_login(request)
      self.assertEqual(response.status_code, 200)

    def test_login_User(self):
        request = self.factory.get("/accounts/login")
        request.user = self.user
        response = account_login(request)
        self.assertEqual(response.status_code, 200)
