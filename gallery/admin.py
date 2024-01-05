from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from embed_video.admin import AdminVideoMixin
from parler.admin import TranslatableAdmin

from .models import Photo, Video


class PhotoAdmin(TranslatableAdmin):

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
        Override the save_model method to create translations for the photo
        """
        super().save_model(request, obj, form, change)
        if not obj.has_translation(obj.get_switch_language()):
            obj.create_translation(
                obj.get_switch_language(),
                title=obj.title,
                image=obj.image,
                description=obj.description,
                date=obj.date,
                live=obj.live,
            )


class VideoAdmin(AdminVideoMixin, TranslatableAdmin):

    list_display = ('title', 'date', 'live')
    list_filter = ('translations__live', 'translations__date')

    def save_model(self, request, obj, form, change):
        """
        Override the save_model method to create translations for the video
        """
        super().save_model(request, obj, form, change)
        if not obj.has_translation(obj.get_switch_language()):
            obj.create_translation(
                obj.get_switch_language(),
                title=obj.title,
                description=obj.description,
                video=obj.video,
                live=obj.live,
            )


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
