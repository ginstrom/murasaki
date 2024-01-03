"""
This module contains utility functions that are used in multiple apps.
"""
from django.utils import translation


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


def get_switch_language_url(url_getter, language_code):
    """
    Gets the switch language URL for the page
    """
    if language_code == 'en':
        return {
            'url': url_getter('ja'),
            'label': '日本語',
            'code': 'ja',
        }
    return {
        'url': url_getter('en'),
        'label': 'English',
        'code': 'en',
    }
