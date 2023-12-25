"""
Models for the pages app.
"""
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
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

    def __str__(self):
        return self.title


