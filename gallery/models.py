"""
Models for the gallery app.

This app is used to display photos and videos.
Photos have a title, description, and image.
Videos have a title, description, and video URL.

Models are translatable using django-parler.
"""
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField
from parler.models import TranslatableModel, TranslatedFields

from common.utils import UrlSwitcher


class Photo(TranslatableModel, UrlSwitcher):
    """
    Represents a photo in the gallery.
    """
    translations = TranslatedFields(
        title=models.CharField(_("title"), max_length=512),
        description=RichTextField(_("description"), blank=True),
        image=models.ImageField(_("image"), upload_to="gallery/photos"),
        live=models.BooleanField(_('live'), default=True),
        date=models.DateTimeField(_('date'), auto_now_add=True),
    )

    def get_absolute_url(self):
        """
        Returns the URL for this page.
        """
        return reverse("photo-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Video(TranslatableModel, UrlSwitcher):
    """
    Represents an embedded video in the gallery.
    """
    translations = TranslatedFields(
        title=models.CharField(_("title"), max_length=512),
        description=RichTextField(_("description"), blank=True),
        video=EmbedVideoField(_("video")),
        live=models.BooleanField(_('live'), default=True),
        date=models.DateTimeField(_('date'), auto_now_add=True),
    )

    def get_absolute_url(self):
        """
        Returns the URL for this page.
        """
        return reverse("video-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title