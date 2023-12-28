from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Page, NewsItem, TourDate


class TourDateAdmin(TranslatableAdmin):
    pass

admin.site.register(Page, TranslatableAdmin)
admin.site.register(NewsItem, TranslatableAdmin)
admin.site.register(TourDate, TourDateAdmin)
