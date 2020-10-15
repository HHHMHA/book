import pytest
from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse

from pages.views import HomePageView


class TestHomePageUrls:
    def test_resolve_url(self):
        assert reverse('home') == '/en/'

    def test_right_view_from_url(self):
        assert resolve('/en/').view_name == 'home'

    def test_right_function_called(self):
        assert resolve('/en/').func.__name__ == HomePageView.as_view().__name__

    def test_home_template_used(self):
        client = Client()
        response = client.get(reverse('home'))
        assertTemplateUsed(response, 'home.html')
