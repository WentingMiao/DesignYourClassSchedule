from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .views import *


class dashboardTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='miao', email='miao@gmail', password='password')


    def test_index_anoymousUser(self):
         request = self.factory.get("/")
         request.user = AnonymousUser()
         response = index(request)
         self.assertEqual(response.status_code, 200)

    def test_index_User(self):
        request = self.factory.get("/")
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)
