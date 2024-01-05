"""
Unit tests for the admin module.

Tests for the custom `save_model()' override and the `thumbnail()' method
"""

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from gallery.admin import PhotoAdmin, VideoAdmin
from gallery.models import Photo, Video


class PhotoAdminTests(TestCase):
    """
    Test the save_model() override and thumbnail() method for the PhotoAdmin class
    """

    def tearDown(self) -> None:
        Photo.objects.all().delete()

    def test_save_model(self):
        """
        Test that the save_model() override creates a translation
        """
        admin = PhotoAdmin(model=Photo, admin_site=None)
        obj = Photo(
            title="Test Photo",
            image="test.jpg",
            description="Test Description",
            date="2019-01-01",
            live=True,
        )
        admin.save_model(request=None, obj=obj, form=None, change=None)
        self.assertTrue(obj.has_translation(obj.get_switch_language()))

    def test_thumbnail(self):
        """
        Test that the thumbnail() method returns an image tag
        """
        admin = PhotoAdmin(model=Photo, admin_site=None)
        obj = Photo(
            title="Test Photo",
            image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
            description="Test Description",
            date="2019-01-01",
            live=True,
        )
        self.assertEqual(admin.thumbnail(obj), '<img src="/media/test.jpg" width="100" height="100" />')

    def test_thumbnail_no_image(self):
        """
        Test that the thumbnail() method returns a dash when there is no image
        """
        admin = PhotoAdmin(model=Photo, admin_site=None)
        obj = Photo(
            title="Test Photo",
            description="Test Description",
            date="2019-01-01",
            live=True,
        )
        self.assertEqual(admin.thumbnail(obj), '-')

    def test_thumbnail_invalid_image(self):
        """
        Test that the thumbnail() method returns a dash when the image is invalid
        """
        admin = PhotoAdmin(model=Photo, admin_site=None)
        obj = Photo(
            title="Test Photo",
            description="Test Description",
            image="test.txt",
        )
        self.assertEqual(admin.thumbnail(obj), '-')


class VideoAdminTests(TestCase):
    """
    Test the save_model() override for the VideoAdmin class
    """

    def tearDown(self) -> None:
        Video.objects.all().delete()

    def test_save_model(self):
        """
        Test that the save_model() override creates a translation
        """
        admin = VideoAdmin(model=Video, admin_site=None)
        obj = Video(
            title="Test Video",
            description="Test Description",
            video='https://www.youtube.com/watch?v=9bZkp7q19f0',
            live=True,
        )
        admin.save_model(request=None, obj=obj, form=None, change=None)
        self.assertTrue(obj.has_translation(obj.get_switch_language()))
