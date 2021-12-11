from django.test import TestCase

from .models import Link
from .views import add_url, generate_code, show_url

class LinkModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = 'https://www.youtube.com/watch?v=kJQP7kiw5Fk&t=2s&ab_channel=LuisFonsiVEVO'
        cls.code = 'GGGG8888'
        cls.link_instance = Link.objects.create(url=cls.url, code=cls.code)

    def test_model_link_return_value(self):
        """
        Testing Links model return value.
        """
        self.link = str(self.link_instance)
        correct_response = f'{self.url} - {self.code}'

        self.assertEqual(self.link, correct_response)

    def tearDown(self):
        self.link_instance.delete()
