from django.test import TestCase

HTTP_OK = 200
HTTP_REDIRECT = 302


class HomePageTest(TestCase):
    def test_get_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTP_REDIRECT)
