from django.test import TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse
import json

class TestCase(TestCase):
    """docstring forTestCase."""
    print(reverse('index'))
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.history_url = reverse('profile')
        # User.objects.create_user('homer', 'ho...@simpson.net', 'simpson')
        user = User.objects.create_user('homer')
        user.set_password('simpson')
        user.save()

    def test_index_login(self):
        self.assertTrue(self.client.login(username='homer',password='simpson'))
        print("User login test successfull.")

    def test_index_GET(self):

        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'user/index.html')

    def test_profile_history(self):

        if(self.client.login(username='homer',password='simpson')):

            response = self.client.get(self.history_url)
            self.assertEquals(response.status_code,200)
        # self.assertTemplateUsed(response,'user/profile')
