"""
Site views
"""
from django.shortcuts import render
from .models import Page


def get_page_or_default(page_type: str, language_code: str='en'):
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


def get_page_context(page_type, language_code):
    """
    Creates the page context dict from the page type and language code.
    """
    return {
        'page': get_page_or_default(page_type, language_code=language_code)
    }


def home(request):
    """
    Serves the site homepage
    """
    context = get_page_context("home", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/home.html", context)


def news(request):
    """
    Serves the site news page
    """
    context = get_page_context("news", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/home.html", context)


def tour(request):
    """
    Serves the site tour page
    """
    context = get_page_context("tour", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/home.html", context)


def music(request):
    """
    Serves the site music page
    """
    context = get_page_context("music", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/home.html", context)


def band(request):
    """
    Serves the site band page
    """
    context = get_page_context("band", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/home.html", context)


def shop(request):
    """
    Serves the site shop page
    """
    context = get_page_context("shop", language_code=request.LANGUAGE_CODE)
    return render(request, "pages/home.html", context)
