from django.conf.urls import url

from . import views

urlpatterns = [
    url("test", views.test, name='test'),
    url('film', views.film),  
    url('show',views.show),  
    url('edit/<int:id>', views.edit),  
    url('update/<int:id>', views.update),  
    url('delete/<int:id>', views.destroy),  
    url("", views.index, name='index'),
    
]