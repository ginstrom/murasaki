from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Page, NewsItem, TourDate


class PageAdmin(TranslatableAdmin):
    list_display = ('title', 'page_type')


class TourDateAdmin(TranslatableAdmin):
    list_display = ('title', 'date', 'venue', 'live')


class NewsItemAdmin(TranslatableAdmin):
    list_display = ('title', 'date', 'live')


admin.site.register(Page, PageAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(TourDate, TourDateAdmin)
