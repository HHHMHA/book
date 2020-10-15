import pytest

from pages.views import HomePageView

pytestmark = pytest.mark.django_db


class TestHomePageView:
    def test_template_name(self):
        view = HomePageView
        assert view.template_name == 'home.html'

