from django.urls import path

from.views import HomePageView, AboutPageView, PolicyPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('policy/', PolicyPageView.as_view(), name='about'),
    ]