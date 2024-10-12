from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/dashboard.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'
    
class ImagesPageView(TemplateView):
    template_name = 'app/images.html'
