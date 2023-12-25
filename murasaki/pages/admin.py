from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Page

admin.site.register(Page, TranslatableAdmin)
