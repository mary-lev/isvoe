import status as status
from django.test import TestCase
from django.urls import reverse_lazy


class TestIndexView(TestCase):

    def test_get(self):
        url = reverse_lazy('isite:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('isite/index.html')

