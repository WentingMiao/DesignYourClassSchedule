from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .views import *
class loginTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_login_anoymousUser(self):
      request = self.factory.get("/accounts/login")
      request.user = AnonymousUser()
      response = account_login(request)
      self.assertEqual(response.status_code, 200)

