from django.test import TestCase
from django.urls import reverse

HTTP_OK = 200
HTTP_REDIRECT = 302
HTTP_REDIRECT_MOVED = 301


class HomePageTest(TestCase):
    def test_get_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTP_REDIRECT)

    def test_get_arabic_by_url(self):
        response = self.client.get("/ar")
        self.assertEqual(response.status_code, HTTP_REDIRECT_MOVED)

    def test_get_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, HTTP_OK)

    def test_right_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

