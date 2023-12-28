from datetime import datetime

from django.test import TestCase
from django.utils import translation

from pages.models import Page, NewsItem, TourDate, MusicRelease


class PageModelTests(TestCase):
    """
    test page creation/translation
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create a page object
        """
        page = Page.objects.create(
            title="Home",
            intro="Homepage",
            page_type="home",
        )
        page.set_current_language("ja")
        page.title = "トップ"
        page.intro = "ホームページ"
        page.page_type = "home"
        page.save()

    @classmethod
    def tearDownClass(cls):
        """
        Delete the page object
        """
        Page.objects.get(translations__title="Home").delete()
        assert Page.objects.count() == 0, Page.objects.all()

    def test_default_page(self):
        """
        Test that the page was created
        """
        page = Page.objects.get(translations__title="Home")
        self.assertEqual(page.title, "Home")
        self.assertEqual(page.page_type, "home")

    def test_english_page(self):
        """
        Test that the page was created
        """
        page = Page.objects.get(translations__title="Home")
        page.set_current_language("en")
        self.assertEqual(page.title, "Home")
        self.assertEqual(page.page_type, "home")

    def test_japanese_page(self):
        """
        Test that the Japanese page was created
        """
        page = Page.objects.get(translations__title="トップ")
        page.set_current_language("ja")
        self.assertEqual(page.title, "トップ")
        self.assertEqual(page.page_type, "home")

    def test_get_absolute_url(self):
        """
        Test that the get_absolute_url method works
        """
        page = Page.objects.get(translations__title="Home")
        with translation.override("en"):
            self.assertEqual(page.get_absolute_url(), "/en/")
        with translation.override("ja"):
            self.assertEqual(page.get_absolute_url(), "/ja/")

    def test_get_absolute_url_for(self):
        """
        Test that the get_absolute_url_for method works
        """
        page = Page.objects.get(translations__title="Home")
        self.assertEqual(page.get_absolute_url_for("en"), "/en/")
        self.assertEqual(page.get_absolute_url_for("ja"), "/ja/")


class NewsItemTests(TestCase):
    """
    test news item creation/translation
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create a news item object
        """
        news_item = NewsItem.objects.create(
            title="News Item",
            body="This is a news item.",
            live=True,
            image="news/news_item.jpg",
        )
        news_item.set_current_language("ja")
        news_item.title = "ニュース"
        news_item.body = "これはニュースです。"
        news_item.live = True
        news_item.image = "news/news_item.jpg"
        news_item.save()

    @classmethod
    def tearDownClass(cls):
        """
        Delete the news item object
        """
        NewsItem.objects.get(translations__title="News Item").delete()
        assert NewsItem.objects.count() == 0, NewsItem.objects.all()

    def test_default_news_item(self):
        """
        Test that the news item was created
        """
        news_item = NewsItem.objects.get(translations__title="News Item")
        self.assertEqual(news_item.title, "News Item")
        self.assertEqual(news_item.body, "This is a news item.")
        self.assertEqual(news_item.live, True)
        self.assertEqual(news_item.image, "news/news_item.jpg")

    def test_english_news_item(self):
        """
        Test that the news item was created
        """
        news_item = NewsItem.objects.get(translations__title="News Item")
        news_item.set_current_language("en")
        self.assertEqual(news_item.title, "News Item")
        self.assertEqual(news_item.body, "This is a news item.")
        self.assertEqual(news_item.live, True)
        self.assertEqual(news_item.image, "news/news_item.jpg")

    def test_japanese_news_item(self):
        """
        Test that the Japanese news item was created
        """
        news_item = NewsItem.objects.get(translations__title="ニュース")
        news_item.set_current_language("ja")
        self.assertEqual(news_item.title, "ニュース")
        self.assertEqual(news_item.body, "これはニュースです。")
        self.assertEqual(news_item.live, True)
        self.assertEqual(news_item.image, "news/news_item.jpg")


class TourDateTests(TestCase):
    """
    test tour date creation/translation
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create a tour date object
        """
        # today's date
        today = datetime.date(datetime.now())
        tour_date = TourDate.objects.create(
            date=today,
            venue="Venue",
            live=True,
        )
        tour_date.set_current_language("ja")
        tour_date.date = today
        tour_date.venue = "会場"
        tour_date.live = True
        tour_date.save()

    @classmethod
    def tearDownClass(cls):
        """
        Delete the tour date object
        """
        TourDate.objects.get(translations__venue="Venue").delete()
        assert TourDate.objects.count() == 0, TourDate.objects.all()

    def test_default_tour_date(self):
        """
        Test that the tour date was created
        """
        tour_date = TourDate.objects.get(translations__venue="Venue")
        self.assertGreaterEqual(tour_date.date.year, 2023)
        self.assertEqual(tour_date.venue, "Venue")
        self.assertEqual(tour_date.live, True)

    def test_english_tour_date(self):
        """
        Test that the tour date was created
        """
        tour_date = TourDate.objects.get(translations__venue="Venue")
        tour_date.set_current_language("en")
        self.assertGreaterEqual(tour_date.date.year, 2023)
        self.assertEqual(tour_date.venue, "Venue")
        self.assertEqual(tour_date.live, True)

    def test_japanese_tour_date(self):
        """
        Test that the Japanese tour date was created
        """
        tour_date = TourDate.objects.get(translations__venue="会場")
        tour_date.set_current_language("ja")
        self.assertGreaterEqual(tour_date.date.year, 2023)
        self.assertEqual(tour_date.venue, "会場")
        self.assertEqual(tour_date.live, True)