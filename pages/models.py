"""
Models for the pages app.
"""
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class UrlSwitcher:
    def get_absolute_url_for(self, language_code):
        """
        Returns the URL for this page in the specified language.
        """
        with translation.override(language_code):
            return self.get_absolute_url()

    def get_switch_language(self):
        """
        If the current language is English, return Japanese, and vice versa.
        """
        if self.get_current_language() == "en":
            return "ja"
        else:
            return "en"


class Page(TranslatableModel, UrlSwitcher):
    """
    Represents one of the top-level pages accessed from the nav bar:
    - Home
    - Band
    - Music
    - Tour
    - News
    - Shop
    """
    class PageType(models.TextChoices):
        """
        Enum for the page types.
        """
        HOME = "home", _("Home")
        BAND = "band", _("Band")
        MUSIC = "music", _("Music")
        TOUR = "tour", _("Tour")
        NEWS = "news", _("News")
        SHOP = "shop", _("Shop")

    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=200),
        intro=RichTextUploadingField(_('intro'), blank=True),
        page_type=models.CharField(
            _("page type"),
            max_length=5,
            choices=PageType.choices,
            default=PageType.HOME,
        ),
    )

    def get_absolute_url(self):
        """
        Returns the URL for this page.
        """
        return reverse(self.page_type)

    def __str__(self):
        return self.title


class NewsItem(TranslatableModel, UrlSwitcher):
    """
    Represents a news item.
    """
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=300),
        body=RichTextUploadingField(_('body'), blank=True),
        live=models.BooleanField(_('live'), default=False),
        date=models.DateTimeField(_('date'), auto_now_add=True),
        image=models.ImageField(_('image'), upload_to="news", blank=True),
    )

    def get_absolute_url(self):
        """
        Returns the URL for this page.
        """
        return reverse("news-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class TourDate(TranslatableModel, UrlSwitcher):
    """
    Represents a tour date.
    """
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=300),
        venue=models.CharField(_('venue'), max_length=300, blank=True),
        description=RichTextUploadingField(_('description'), blank=True),
        date=models.DateField(_('date')),
        live=models.BooleanField(_('live'), default=False),
    )

    def get_absolute_url(self):
        """
        Returns the URL for this page.
        """
        return reverse("tour-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title