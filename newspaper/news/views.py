from django.shortcuts import render
from .models import New
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.critical('hello!')
    news = New.objects.all()
    return render(request, 'news/index.html', context={'news': news})


def detail(request, slug):
    news = New.objects.all()
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'new': new, 'news': news})
