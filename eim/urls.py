from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^UnitList/', views.UnitList, name='unit_list'),
    url(r'^UnitCreate/', views.UnitCreate, name='unit_create'),
    url(r'^OldKcsCreate/', views.OldKcsCreate, name='OldKcs_create'),
    url(r'^receive/', views.OldKcsList, name='oldkcs_receive'),
    url(r'^home/', views.home, name='home'),
    url(r'^', views.home, name='home'),
]
