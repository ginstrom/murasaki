from django.contrib import admin
from parler.admin import TranslatableAdmin
from imagekit.admin import AdminThumbnail

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

    thumbnail = AdminThumbnail(image_field='image')

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
