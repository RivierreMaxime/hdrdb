from django.conf.urls import url

from . import views

urlpatterns = [
    url("listing", views.listing, name='listing'),
    url('news', views.news, name='news'),
]