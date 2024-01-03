from django.core.paginator import Paginator
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
    """
    Shows the photos page. Photos are paginated.
    """
    photos = Photo.objects.translated(live=True).order_by("-translations__date")
    get_url = url_getter('photos')
    context = {
        'switch_language': get_switch_language_url(get_url, request.LANGUAGE_CODE),
        'photos': Paginator(photos, 16).get_page(request.GET.get('page', 1)),
        'absolute_url': get_url(request.LANGUAGE_CODE),
    }
    return render(request, "gallery/photos.html", context)


def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        'switch_language': get_switch_language_url(photo.get_absolute_url_for, request.LANGUAGE_CODE),
        'photo': photo,
    }
    return render(request, "gallery/photo_detail.html", context)


def videos(request):
    """
    Shows the videos page. Videos are paginated.
    """
    videos = Video.objects.translated(live=True).order_by("-translations__date")
    get_url = url_getter('videos')
    context = {
        'switch_language': get_switch_language_url(get_url, request.LANGUAGE_CODE),
        'videos': Paginator(videos, 6).get_page(request.GET.get('page', 1)),
        'absolute_url': get_url(request.LANGUAGE_CODE),
    }
    return render(request, "gallery/videos.html", context)


def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    context = {
        'switch_language': get_switch_language_url(video.get_absolute_url_for, request.LANGUAGE_CODE),
        'video': video,
    }
    return render(request, "gallery/video_detail.html", context)