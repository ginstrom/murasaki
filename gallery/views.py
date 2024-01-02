from django.shortcuts import render

from .models import Photo, Video
from common.utils import get_switch_language_url


def url_getter(page):
    """
    Returns a function that gets the URL for the specified page.
    """
    def get_url(language_code):
        if language_code == 'en':
            return f'/en/gallery/{page}/'
        return f'/ja/gallery/{page}/'

    return get_url


def photos(request):
    context = {
        'switch_language': get_switch_language_url(url_getter('photos'), request.LANGUAGE_CODE),
    }
    return render(request, "gallery/photos.html", context)


def photo_detail(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    context = {
        'switch_language': get_switch_language_url(photo.get_absolute_url_for, request.LANGUAGE_CODE),
    }
    return render(request, "gallery/photo_detail.html", context)


def videos(request):
    context = {
        'switch_language': get_switch_language_url(url_getter('videos'), request.LANGUAGE_CODE),
    }
    return render(request, "gallery/videos.html", context)


def video_detail(request, video_id):
    video = Video.objects.get(pk=video_id)
    context = {
        'switch_language': get_switch_language_url(video.get_absolute_url_for, request.LANGUAGE_CODE),
    }
    return render(request, "gallery/video_detail.html", context)