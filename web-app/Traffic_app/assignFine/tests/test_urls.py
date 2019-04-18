from django.test import SimpleTestCase
from django.urls import reverse, resolve
from assignFine.views import fine

class TestUrls(SimpleTestCase):
    """docstring for."""
    def test_assignFine_url_resolved(self):
        url = reverse('assignFine')
        self.assertEquals(resolve(url).func,fine)
