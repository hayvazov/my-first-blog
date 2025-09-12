from django.test import TestCase
from django.urls import reverse


class LimpiezaDeSofasViewTest(TestCase):
    def test_page_exists(self):
        response = self.client.get(reverse('limpieza_de_sofas'))
        self.assertEqual(response.status_code, 200)
