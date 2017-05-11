from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^OldKcsCreate/', views.OldKcsCreate, name='OldKcs_create'),
    url(r'^receive/', views.OldKcsList, name='receive_kcs'),
    url(r'^home/', views.home, name='home'),
    url(r'^', views.home, name='home'),
]
