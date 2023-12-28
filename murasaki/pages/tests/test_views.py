"""
Unit tests for pages views
"""

from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from pages.models import Page, NewsItem, TourDate, MusicRelease

class DefaultPageViewTests(TestCase):
    """
    Navigate to each of the top-level pages, and make
    sure that a default page is displayed.
    """
    def setUp(self) -> None:
        """
        Set up the test case
        """
        self.pages = [
            ("/", "pages/home.html"),
            ("/band/", "pages/band.html"),
            ("/music/", "pages/music.html"),
            ("/news/", "pages/news.html"),
            ("/shop/", "pages/shop.html"),
            ("/tour/", "pages/tour.html"),
        ]
        assert Page.objects.count() == 0, Page.objects.all()

    def tearDown(self) -> None:
        Page.objects.all().delete()

    def test_default_page_views_redirect(self):
        """
        Test that we redirect from top level
        """
        for page, templ in self.pages:
            response = self.client.get(page)
            self.assertRedirects(
                response,
                '/en{}'.format(page),
                status_code=302,
                target_status_code=200,
                fetch_redirect_response=True)

    def test_default_page_views(self):
        """
        Test that the pages are accessible
        """
        for page, templ in self.pages:
            response = self.client.get(page, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, templ)

    def test_english_page_views(self):
        """
        Test that the English pages are accessible
        """
        for page, templ in self.pages:
            response = self.client.get('/en{}'.format(page))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, templ)

    def test_japanese_page_views(self):
        """
        Test that the Japanese pages are accessible
        """
        for page, templ in self.pages:
            response = self.client.get('/ja{}'.format(page))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, templ)

    def test_each_page_type_english(self):
        """
        Test reverse() function with English
        """
        with translation.override("en"):
            for page_type in Page.PageType:
                response = self.client.get(reverse(page_type))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, "pages/{}.html".format(page_type))

    def test_each_page_type_japanese(self):
        """
        Test reverse() function with Japanese
        """
        with translation.override("ja"):
            for page_type in Page.PageType:
                response = self.client.get(reverse(page_type))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, "pages/{}.html".format(page_type))
