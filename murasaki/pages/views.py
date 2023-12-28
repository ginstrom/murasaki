"""
Site views
"""
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Page, NewsItem, TourDate


def get_page_or_default(page_type: str, language_code: str = 'en'):
    """
    Gets the Page object with the specified page type,
    or creates a default object
    """
    page = Page.objects.language(language_code).filter(translations__page_type=page_type).first()
    if page:
        return page
    page = Page()
    page.set_current_language('en')
    for label, name in Page.PageType.choices:
        if label == page_type:
            page.title = name
            page.page_type = label
            page.save()
            page.set_current_language(language_code)
            return page


def get_switch_language_url(page, language_code):
    """
    Gets the switch language URL for the page
    """
    if language_code == 'en':
        return {
            'url': page.get_absolute_url_for('ja'),
            'label': '日本語',
            'code': 'ja',
        }
    return {
        'url': page.get_absolute_url_for('en'),
        'label': 'English',
        'code': 'en',
    }


def get_page_context(page_type, language_code):
    """
    Creates the page context dict from the page type and language code.
    """
    page = get_page_or_default(page_type, language_code=language_code)
    return {
        'page': page,
        'switch_language': get_switch_language_url(page, language_code),
    }


def home(request):
    """
    Serves the site homepage
    """
    context = get_page_context("home", language_code=request.LANGUAGE_CODE)
    # Add 4 latest news items to the context
    context['news_items'] = NewsItem.objects.translated(request.LANGUAGE_CODE).filter(translations__live=True).order_by("-translations__date")[:4]
    # Add 4 latest tour dates to the context
    context['tour_dates'] = TourDate.objects.translated(request.LANGUAGE_CODE).order_by("-translations__date")[:4]
    return render(request, "pages/home.html", context)


def news(request):
    """
    Serves the site news page
    """
    context = get_page_context("news", language_code=request.LANGUAGE_CODE)
    page = request.GET.get("page", 1)
    news_items = NewsItem.objects.translated(request.LANGUAGE_CODE).filter(translations__live=True).order_by("-translations__date")
    context['news_items'] = Paginator(news_items, 10).get_page(page)
    return render(request, "pages/news.html", context)


def tour(request):
    """
    Serves the site tour page
    """
    context = get_page_context("tour", language_code=request.LANGUAGE_CODE)
    page = request.GET.get("page", 1)
    tour_dates = TourDate.objects.translated(request.LANGUAGE_CODE).filter(translations__live=True).order_by("-translations__date")
    context['tour_dates'] = Paginator(tour_dates, 10).get_page(page)
    return render(request, "pages/tour.html", context)


def music(request):
    """
    Serves the site music page
    """
    context = get_page_context("music", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/music.html", context)


def band(request):
    """
    Serves the site band page
    """
    context = get_page_context("band", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/band.html", context)


def shop(request):
    """
    Serves the site shop page
    """
    context = get_page_context("shop", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/shop.html", context)
