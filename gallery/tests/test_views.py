"""
Unit tests for the gallery views module.
"""
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from gallery.models import Photo, Video
from gallery import views


def test_url_getter():
    """
    Test that the url_getter() function returns a function that returns the correct URL
    """
    get_url = views.url_getter('photos')
    assert get_url('en') == '/en/gallery/photos/'
    assert get_url('ja') == '/ja/gallery/photos/'

    get_url = views.url_getter('videos')
    assert get_url('en') == '/en/gallery/videos/'
    assert get_url('ja') == '/ja/gallery/videos/'


class GalleryViewTests(TestCase):
    """
    Test the gallery views
    """

    def setUp(self) -> None:
        self.photo = Photo.objects.create(
            title="Test Photo",
            image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
            description="Test Photo Description",
        )
        self.video = Video.objects.create(
            title="Test Video",
            video="https://www.youtube.com/watch?v=9bZkp7q19f0",
            description="Test Video Description",
        )

    def tearDown(self) -> None:
        Photo.objects.all().delete()
        Video.objects.all().delete()

    def test_photos_view(self):
        """
        Test that the photos view returns the correct response
        """
        response = self.client.get('/gallery/photos/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/photos.html')

    def test_videos_view(self):
        """
        Test that the videos view returns the correct response
        """
        response = self.client.get('/gallery/videos/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/videos.html')

    def test_photo_detail_view(self):
        """
        Test that the photo detail view returns the correct response
        """
        response = self.client.get(f'/gallery/photos/{self.photo.pk}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/photo_detail.html')

    def test_video_detail_view(self):
        """
        Test that the video detail view returns the correct response
        """
        response = self.client.get(f'/gallery/videos/{self.video.pk}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/video_detail.html')