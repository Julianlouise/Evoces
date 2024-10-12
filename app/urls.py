from django.urls import path
from .views import HomePageView, AboutPageView, ImagesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='dashboard'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('images/', ImagesPageView.as_view(), name='images'),
]
