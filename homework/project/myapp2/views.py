from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import logging


logger = logging.getLogger(__name__)

def index(request):
    logger.info('index page accessed')
    Response = render_to_string("myapp2/main.html")
    return HttpResponse(Response)

def about(request):
    logger.info('about page accessed')
    Response = render_to_string("myapp2/about.html")
    return HttpResponse(Response)