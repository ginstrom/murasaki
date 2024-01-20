"""
Site views
"""
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Page, NewsItem, TourDate

from common.utils import get_switch_language_url


def get_page_or_default(page_type: str, language_code: str = 'en'):
    """
    Gets the Page object with the specified page type,
    or creates a default object
    """
    page = Page.objects.translated(page_type=page_type).first()
    if page:
        return page

    # Create a default page
    page = Page()
    page.set_current_language('en')
    for label, name in Page.PageType.choices:
        if label == page_type:
            page.title = name
            page.page_type = label
            page.save()
            page.create_translation(
                'ja',
                title=name,
                page_type=label,
                live=True,
            )
            page.set_current_language(language_code)
            return page


def get_page_context(page_type, language_code):
    """
    Creates the page context dict from the page type and language code.
    """
    page = get_page_or_default(page_type, language_code=language_code)
    url_getter = page.get_absolute_url_for
    return {
        'page': page,
        'switch_language': get_switch_language_url(url_getter, language_code),
    }


def live_objects(model, language_code: str = 'en'):
    """
    Returns the live objects for the specified model
    """
    return model.objects.translated(language_code, live=True).order_by("-translations__date")


def home(request):
    """
    Serves the site homepage
    """
    language = request.LANGUAGE_CODE
    context = get_page_context("home", language_code=language)
    # Add 4 latest news items to the context
    news_items = live_objects(NewsItem, language)
    context['news_items'] = news_items[:4]
    # Add 4 latest tour dates to the context
    tour_dates = live_objects(TourDate, language)
    context['tour_dates'] = tour_dates[:4]
    return render(request, "pages/home.html", context)


def news(request):
    """
    Serves the site news page
    """
    language = request.LANGUAGE_CODE
    context = get_page_context("news", language_code=language)
    page = request.GET.get("page", 1)
    news_items = live_objects(NewsItem, language)
    context['news_items'] = Paginator(news_items, 10).get_page(page)
    return render(request, "pages/news.html", context)


def news_detail(request, pk):
    """
    Serves the site news detail page
    """
    language = request.LANGUAGE_CODE
    context = get_page_context("news", language_code=language)
    news_item = NewsItem.objects.get(pk=pk)
    context['news_item'] = news_item
    url_getter = news_item.get_absolute_url_for
    context['switch_language'] = get_switch_language_url(url_getter, language_code=language)
    return render(request, "pages/news_detail.html", context)


def tour(request):
    """
    Serves the site tour page
    """
    language = request.LANGUAGE_CODE
    context = get_page_context("tour", language_code=language)
    page = request.GET.get("page", 1)
    tour_dates = live_objects(TourDate, language)
    context['tour_dates'] = Paginator(tour_dates, 10).get_page(page)
    return render(request, "pages/tour.html", context)


def tour_detail(request, pk):
    """
    Serves the site tour detail page
    """
    language = request.LANGUAGE_CODE
    context = get_page_context("tour", language_code=language)
    tour_date = TourDate.objects.get(pk=pk)
    context['tour_date'] = tour_date
    url_getter = tour_date.get_absolute_url_for
    context['switch_language'] = get_switch_language_url(url_getter, language_code=language)
    return render(request, "pages/tour_detail.html", context)


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
