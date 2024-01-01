from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin

from .models import Page, NewsItem, TourDate


class PageAdmin(TranslatableAdmin):
    list_display = ('title', 'page_type')


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
                width = min(obj.image.width, 100)
                height = min(obj.image.height, 100)
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
