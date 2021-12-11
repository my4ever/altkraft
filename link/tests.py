from django.test import TestCase

from .models import Link
from .views import add_url, generate_code, show_url

class LinkModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'https://www.youtube.com/watch?v=kJQP7kiw5Fk&t=2s&ab_channel=LuisFonsiVEVO'
        cls.code = 'GGGG8888'

