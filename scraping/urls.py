from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("listing", views.listing, name='listing'),
    path('news', views.news, name='news'),
    path('coming', views.coming, name='coming')
]