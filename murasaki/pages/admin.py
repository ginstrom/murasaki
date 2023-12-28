from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Page, NewsItem, TourDate, MusicRelease

admin.site.register(Page, TranslatableAdmin)
admin.site.register(NewsItem, TranslatableAdmin)
admin.site.register(TourDate, TranslatableAdmin)
admin.site.register(MusicRelease, TranslatableAdmin)
