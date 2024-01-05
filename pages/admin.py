from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin

from .models import Page, NewsItem, TourDate


class PageAdmin(TranslatableAdmin):
    """
    Admin for the Page model.

    We prevent creation and deletion from the admin interface.
    This is because pages are singletons; we want them created once and not added or removed.

    Additionally, we prevent changing the page type.
    """
    list_display = ('title', 'page_type')
    readonly_fields = ('page_type',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TourDateAdmin(TranslatableAdmin):
    list_display = ('title', 'date', 'venue', 'live')
    list_filter = ('translations__live', 'translations__date')

    def save_model(self, request, obj, form, change):
        """
        Override the save_model method to create translations for the tour date
        """
        super().save_model(request, obj, form, change)
        if not obj.has_translation(obj.get_switch_language()):
            obj.create_translation(
                obj.get_switch_language(),
                title=obj.title,
                venue=obj.venue,
                description=obj.description,
                date=obj.date,
                live=obj.live,
            )


class NewsItemAdmin(TranslatableAdmin):

    def thumbnail(self, obj):
        """
        Return a thumbnail of the image
        """
        if obj.image:
            try:
                width = min(obj.image.width or 100, 100)
                height = min(obj.image.height or 100, 100)
                return mark_safe(f'<img src="{obj.image.url}" width="{width}" height="{height}" />')
            except Exception:
                pass
        return '-'
    thumbnail.short_description = _('Thumbnail')

    list_display = ('title', 'date', 'live', 'thumbnail')
    list_filter = ('translations__live', 'translations__date')
    readonly_fields = ('thumbnail',)

    def save_model(self, request, obj, form, change):
        """
        Override the save_model method to create translations for the news item
        """
        super().save_model(request, obj, form, change)
        if not obj.has_translation(obj.get_switch_language()):
            obj.create_translation(
                obj.get_switch_language(),
                title=obj.title,
                body=obj.body,
                live=obj.live,
                image=obj.image,
            )


admin.site.register(Page, PageAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(TourDate, TourDateAdmin)
