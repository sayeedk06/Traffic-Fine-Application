from django.test import TestCase,Client
from django.contrib.auth.models import User
from assignFine.models import Fine
from assignFine.forms import FineForm
from django.urls import reverse
import json

class TestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.fine_url = reverse('assignFine')
        user = User.objects.create_user('darth_vader')
        user.set_password('father')
        user.save()


    def test_fine_form(self):
        if(self.client.login(username='darth_vader',password='father')):

            form = FineForm(data={'amount': 200})
            self.assertTrue(form.is_valid())
            form = FineForm(data={'amount': -200})
            self.assertFalse(form.is_valid())
