from django.shortcuts import render


def get_switch_language_url(page, language_code):
    """
    Gets the switch language URL for the page
    """
    if language_code == 'en':
        return {
            'url': f'/ja/gallery/{page}/',
            'label': '日本語',
            'code': 'ja',
        }
    return {
        'url': f'/en/gallery/{page}/',
        'label': 'English',
        'code': 'en',
    }


def photos(request):
    context = {
        'switch_language': get_switch_language_url('photos', request.LANGUAGE_CODE),
    }
    return render(request, "gallery/photos.html", context)


def videos(request):
    context = {
        'switch_language': get_switch_language_url('videos', request.LANGUAGE_CODE),
    }
    return render(request, "gallery/videos.html", context)
