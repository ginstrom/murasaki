"""
Unit tests for the gallery.models module.
"""

from django.test import TestCase
from django.utils import translation

from gallery.models import Photo, Video


class PhotoModelTests(TestCase):
    """
    Tests for the Photo model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Creates a Photo object for use in tests.
        """
        photo = Photo.objects.create(
            title="Test Photo",
            description="Test Description",
            live=True,
            image="gallery/photos/test-photo.jpg",
        )
        photo.create_translation(
            "ja",
            title="テスト写真",
            description="Test Description",
            live=True,
            image="gallery/photos/test-photo.jpg",
        )
        cls.photo = photo

    @classmethod
    def tearDownClass(cls):
        """
        Deletes the Photo object.
        """
        cls.photo.delete()
        super().tearDownClass()

    def test_get_switch_language_url(self):
        """
        Tests the get_switch_language_url() method.
        """
        photo = Photo.objects.get(pk=self.photo.id)
        assert photo.get_current_language() == "en", "Current language should be English, not Japanese"
        assert photo.get_switch_language() == "ja", "Switch language should be Japanese, not English"
        photo.set_current_language("ja")
        assert photo.get_current_language() == "ja", "Current language should be Japanese, not English"
        assert photo.get_switch_language() == "en", "Switch language should be English, not Japanese"
        photo.set_current_language("en")
        assert photo.get_current_language() == "en", "Current language should be English, not Japanese"
        assert photo.get_switch_language() == "ja", "Switch language should be Japanese, not English"

    def test_str_en(self):
        """
        Tests the __str__() method in English.
        """
        photo = Photo.objects.get(pk=self.photo.id)
        assert str(photo) == "Test Photo", "Photo string representation should be 'Test Photo'"

    def test_str_ja(self):
        """
        Tests the __str__() method in Japanese.
        """
        photo = Photo.objects.get(pk=self.photo.id)
        photo.set_current_language("ja")
        assert str(photo) == "テスト写真", "Photo string representation should be 'テスト写真'"

    def test_get_absolute_url_en(self):
        """
        Tests the get_absolute_url() method in English.
        """
        photo = Photo.objects.get(pk=self.photo.id)
        with translation.override("en"):
            expected = f"/en/gallery/photos/{photo.pk}/"

    def test_get_absolute_url_ja(self):
        """
        Tests the get_absolute_url() method in Japanese.
        """
        photo = Photo.objects.get(pk=self.photo.id)
        with translation.override("ja"):
            expected = f"/ja/gallery/photos/{photo.pk}/"
            assert photo.get_absolute_url() == expected, f"Photo absolute URL should be '{expected}'"


class VideoModelTests(TestCase):
    """
    Tests for the Video model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Creates a Video object for use in tests.
        """
        video = Video.objects.create(
            title="Test Video",
            description="Test Description",
            live=True,
            video="gallery/videos/test-video.mp4",
        )
        video.create_translation(
            "ja",
            title="テストビデオ",
            description="Test Description",
            live=True,
            video="gallery/videos/test-video.mp4",
        )
        cls.video = video

    @classmethod
    def tearDownClass(cls):
        """
        Deletes the Video object.
        """
        cls.video.delete()
        super().tearDownClass()

    def test_get_switch_language_url(self):
        """
        Tests the get_switch_language_url() method.
        """
        video = Video.objects.get(pk=self.video.id)
        assert video.get_current_language() == "en", "Current language should be English, not Japanese"
        assert video.get_switch_language() == "ja", "Switch language should be Japanese, not English"
        video.set_current_language("ja")
        assert video.get_current_language() == "ja", "Current language should be Japanese, not English"
        assert video.get_switch_language() == "en", "Switch language should be English, not Japanese"
        video.set_current_language("en")
        assert video.get_current_language() == "en", "Current language should be English, not Japanese"
        assert video.get_switch_language() == "ja", "Switch language should be Japanese, not English"

    def test_str_en(self):
        """
        Tests the __str__() method in English.
        """
        video = Video.objects.get(pk=self.video.id)
        assert str(video) == "Test Video", "Video string representation should be 'Test Video'"

    def test_str_ja(self):
        """
        Tests the __str__() method in Japanese.
        """
        video = Video.objects.get(pk=self.video.id)
        video.set_current_language("ja")
        assert str(video) == "テストビデオ", "Video string representation should be 'テストビデオ'"

    def test_get_absolute_url_en(self):
        """
        Tests the get_absolute_url() method in English.
        """
        video = Video.objects.get(pk=self.video.id)
        with translation.override("en"):
            expected = f"/en/gallery/videos/{video.pk}/"
            assert video.get_absolute_url() == expected, f"Video absolute URL should be '{expected}'"

    def test_get_absolute_url_ja(self):
        """
        Tests the get_absolute_url() method in Japanese.
        """
        video = Video.objects.get(pk=self.video.id)
        with translation.override("ja"):
            expected = f"/ja/gallery/videos/{video.pk}/"
            assert video.get_absolute_url() == expected, f"Video absolute URL should be '{expected}'"


class PhotoBilingualTests(TestCase):
    """
    Test bilingual handling of photos
    """
    def tearDown(self):
        """
        Deletes all Photo objects.
        """
        Photo.objects.all().delete()

    def test_create_english_item_only(self):
        """
        When we create an English-language photo, no Japanese-language photo should be created.
        """
        photo = Photo.objects.language('en').create(
            title="Test Photo",
            description="Test Description",
            live=True,
            image="gallery/photos/test-photo.jpg",
        )
        assert photo.translations.count() == 1, "There should be one translation"
        japanese_item = Photo.objects.translated("ja").filter(pk=photo.pk)
        assert not japanese_item, japanese_item
        english_item = Photo.objects.translated("en").get(pk=photo.pk)
        assert english_item == photo, english_item

    def test_create_japanese_item_only(self):
        """
        When we create a Japanese-language photo, no English-language photo should be created.
        """
        photo = Photo.objects.language('ja').create(
            title="テスト写真",
            description="Test Description",
            live=True,
            image="gallery/photos/test-photo.jpg",
        )
        assert photo.translations.count() == 1, "There should be one translation"
        english_item = Photo.objects.translated("en").filter(pk=photo.pk)
        assert not english_item, english_item
        japanese_item = Photo.objects.translated("ja").get(pk=photo.pk)
        assert japanese_item == photo, japanese_item


class VideoModelTests(TestCase):
    """
    Tests for the Video model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Creates a Video object for use in tests.
        """
        video = Video.objects.create(
            title="Test Video",
            description="Test Description",
            live=True,
            video="https://youtu.be/1234567890",
        )
        video.create_translation(
            "ja",
            title="テストビデオ",
            description="Test Description",
            live=True,
            video="https://youtu.be/1234567890",
        )
        cls.video = video

    @classmethod
    def tearDownClass(cls):
        """
        Deletes the Video object.
        """
        cls.video.delete()
        super().tearDownClass()

    def test_str_en(self):
        """
        Tests the __str__() method in English.
        """
        video = Video.objects.get(pk=self.video.id)
        assert str(video) == "Test Video", "Video string representation should be 'Test Video'"

    def test_str_ja(self):
        """
        Tests the __str__() method in Japanese.
        """
        video = Video.objects.get(pk=self.video.id)
        video.set_current_language("ja")
        assert str(video) == "テストビデオ", "Video string representation should be 'テストビデオ'"

    def test_get_absolute_url_en(self):
        """
        Tests the get_absolute_url() method in English.
        """
        video = Video.objects.get(pk=self.video.id)
        with translation.override("en"):
            expected = f"/en/gallery/videos/{video.pk}/"
            assert video.get_absolute_url() == expected, f"Video absolute URL should be '{expected}'"

    def test_get_absolute_url_ja(self):
        """
        Tests the get_absolute_url() method in Japanese.
        """
        video = Video.objects.get(pk=self.video.id)
        with translation.override("ja"):
            expected = f"/ja/gallery/videos/{video.pk}/"
            assert video.get_absolute_url() == expected, f"Video absolute URL should be '{expected}'"
