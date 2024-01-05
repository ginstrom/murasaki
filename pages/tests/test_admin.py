"""
Unit tests for the admin module.

Tests for the custom `save_model()' override
"""

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from pages.admin import PageAdmin, TourDateAdmin, NewsItemAdmin
from pages.models import Page, TourDate, NewsItem


class PageAdminTests(TestCase):
    """
    Test the custom functionality of the PageAdmin class:
        - creation prevented
        - deletion prevented
    """

    def tearDown(self) -> None:
        Page.objects.all().delete()

    def test_has_add_permission(self):
        """
        Test that the add permission is disabled
        """
        admin = PageAdmin(model=Page, admin_site=None)
        self.assertFalse(admin.has_add_permission(request=None))

    def test_has_delete_permission(self):
        """
        Test that the delete permission is disabled
        """
        admin = PageAdmin(model=Page, admin_site=None)
        self.assertFalse(admin.has_delete_permission(request=None))


class TourDateAdminTests(TestCase):
    """
    Test:
      - the save_model() override for the TourDateAdmin class
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
    Test:
     - the save_model() override for the NewsItemAdmin class
     - the thumbnail() method for the NewsItemAdmin class
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

    def test_thumbnail_short_description(self):
        """
        Test that the thumbnail() method returns a short description
        """
        admin = NewsItemAdmin(model=NewsItem, admin_site=None)
        self.assertEqual(admin.thumbnail.short_description, "Thumbnail")

    def test_thumbnail(self):
        """
        Test that the thumbnail() method returns an image tag
        """
        admin = NewsItemAdmin(model=NewsItem, admin_site=None)
        obj = NewsItem(
            title="Test News Item",
            body="Test Body",
            image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
            live=True,
        )
        self.assertEqual(admin.thumbnail(obj), '<img src="/media/test.jpg" width="100" height="100" />')

    def test_thumbnail_no_image(self):
        """
        Test that the thumbnail() method returns a dash when there is no image
        """
        admin = NewsItemAdmin(model=NewsItem, admin_site=None)
        obj = NewsItem(
            title="Test News Item",
            body="Test Body",
            live=True,
        )
        self.assertEqual(admin.thumbnail(obj), "-")

    def test_thumbnail_invalid_image(self):
        """
        Test that the thumbnail() method returns a dash when there is an invalid image
        """
        admin = NewsItemAdmin(model=NewsItem, admin_site=None)
        obj = NewsItem(
            title="Test News Item",
            body="Test Body",
            image='foo.txt',
        )
        self.assertEqual(admin.thumbnail(obj), "-")
