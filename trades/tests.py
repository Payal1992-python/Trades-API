from django.test import SimpleTestCase
from django.conf import settings

class SmokeTest(SimpleTestCase):
    def test_settings_loaded(self):
        self.assertTrue(settings.INSTALLED_APPS)
