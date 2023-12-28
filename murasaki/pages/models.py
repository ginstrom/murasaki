"""
Models for the pages app.
"""
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Page(TranslatableModel):
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

    def get_absolute_url_for(self, language_code):
        """
        Returns the URL for this page.
        """
        with translation.override(language_code):
            return self.get_absolute_url()

    def __str__(self):
        return self.title


class NewsItem(TranslatableModel):
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

    def __str__(self):
        return self.title


class TourDate(TranslatableModel):
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

    def __str__(self):
        return self.title