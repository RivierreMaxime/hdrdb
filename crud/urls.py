from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('film', views.film),
    path('test', views.test),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('show', views.show),
    
]