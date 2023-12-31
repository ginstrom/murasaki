"""
Unit tests for the admin module.

Tests for the custom `save_model()' override
"""

from django.test import TestCase

from pages.admin import TourDateAdmin, NewsItemAdmin
from pages.models import TourDate, NewsItem


class TourDateAdminTests(TestCase):
    """
    Test the save_model() override for the TourDateAdmin class
    """

    def tearDown(self) -> None:
        TourDate.objects.all().delete()

    def test_save_model(self):
        """
        Test that the save_model() override creates a translation
        """
        admin = TourDateAdmin(model=TourDate, admin_site=None)
        obj = TourDate(
            title="Test Tour Date",
            venue="Test Venue",
            description="Test Description",
            date="2019-01-01",
            live=True,
        )
        admin.save_model(request=None, obj=obj, form=None, change=None)
        self.assertTrue(obj.has_translation(obj.get_switch_language()))


class NewsItemAdminTests(TestCase):
    """
    Test the save_model() override for the NewsItemAdmin class
    """

    def tearDown(self) -> None:
        NewsItem.objects.all().delete()

    def test_save_model(self):
        """
        Test that the save_model() override creates a translation
        """
        admin = NewsItemAdmin(model=NewsItem, admin_site=None)
        obj = NewsItem(
            title="Test News Item",
            body="Test Body",
            image="test.jpg",
            live=True,
        )
        admin.save_model(request=None, obj=obj, form=None, change=None)
        self.assertTrue(obj.has_translation(obj.get_switch_language()))