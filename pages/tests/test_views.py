"""
Unit tests for pages views
"""

from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from pages import views
from pages.models import Page, NewsItem, TourDate


class TestLiveObjects(TestCase):
    """
    Test the live_objects() function
    """
    def setUp(self) -> None:
        """
        Set up the test case
        """
        self.news_item = NewsItem.objects.language('en').create(
            title="Test News Item",
            body="Test body",
            live=True,
            image='news/default.jpg',
        )
        self.tour_date = TourDate.objects.create(
            title="Test Tour Date",
            venue="Test Venue",
            description="Test Description",
            date="2019-01-01",
            live=True,
        )

    def tearDown(self) -> None:
        """
        Tear down the test case
        """
        NewsItem.objects.all().delete()
        TourDate.objects.all().delete()

    def test_live_objects_news(self):
        """
        Ensure that the correct language only is returned
        """
        self.assertEqual(views.live_objects(NewsItem, 'ja').count(), 0)
        self.assertEqual(views.live_objects(NewsItem, 'en').count(), 1)

    def test_non_live(self):
        """
        Ensure that the correct language only is returned
        """
        self.news_item.live = False
        self.news_item.save()
        self.assertEqual(views.live_objects(NewsItem, 'ja').count(), 0)
        self.assertEqual(views.live_objects(NewsItem, 'en').count(), 0)

    def test_live_objects_tours(self):
        """
        Ensure that the correct language only is returned
        """
        self.assertEqual(views.live_objects(TourDate, 'ja').count(), 0)
        self.assertEqual(views.live_objects(TourDate, 'en').count(), 1)


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

    def test_existing_home_page(self):
        """
        Test that the correct page is retrieved when the page object exists
        """
        Page.objects.create(
            title="Home Test",
            page_type=Page.PageType.HOME,
            intro="Welcome to the test home page",
        )
        response = self.client.get("/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        assert "Home Test" in str(response.content)

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


class NewsItemViewTests(TestCase):
    """
    Test the news item view
    """
    def setUp(self) -> None:
        """
        Set up the test case
        """
        self.news_item = NewsItem.objects.create(
            title="News Item Test",
            body="Welcome to the test news item",
            image="test.jpg",
        )
        assert NewsItem.objects.count() == 1, NewsItem.objects.all()

    def tearDown(self) -> None:
        NewsItem.objects.all().delete()

    def test_existing_news_item(self):
        """
        Test that the correct news item is retrieved when the news item object exists
        """
        response = self.client.get(self.news_item.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/news_detail.html")
        assert "News Item Test" in str(response.content)

    def test_nonexistent_news_item(self):
        """
        Test that a 404 error is raised when the news item object does not exist
        """
        with self.assertRaises(NewsItem.DoesNotExist):
            self.client.get("/en/news/{}/".format(self.news_item.id + 1))


class TourDateViewTests(TestCase):
    """
    Test the tour date view
    """
    def setUp(self) -> None:
        """
        Set up the test case
        """
        self.tour_date = TourDate.objects.create(
            title="Tour Date Test",
            date="2020-01-01",
            venue="Test Venue",
            live=True,
        )
        assert TourDate.objects.count() == 1, TourDate.objects.all()

    def tearDown(self) -> None:
        TourDate.objects.all().delete()

    def test_existing_tour_date(self):
        """
        Test that the correct tour date is retrieved when the tour date object exists
        """
        response = self.client.get(self.tour_date.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/tour_detail.html")
        assert "Tour Date Test" in str(response.content)

    def test_nonexistent_tour_date(self):
        """
        Test that a 404 error is raised when the tour date object does not exist
        """
        with self.assertRaises(TourDate.DoesNotExist):
            self.client.get("/en/tour/{}/".format(self.tour_date.id + 1))