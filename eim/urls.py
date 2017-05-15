from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^component_detail/(?P<id>[0-9]+)', views.ComponentDetail, name='component_detail'),
    url(r'^inventory/', views.ShowInventory, name='show_inventory'),
    url(r'^TargetValidation/',views.TergetValidation, name='target_validation'),
    url(r'^OperationCreate/', views.OperationCreate, name='operation_create'),
    url(r'^OperationList/', views.OperationList, name='operation_list'),
    url(r'^OperationDetail/(?P<id>[0-9]+)/$', views.OperationDetail, name='operation_detail'),
    url(r'^UnitDetail/(?P<id>[0-9]+)/$', views.UnitDetail, name='unit_detail'),
    url(r'^UnitList/', views.UnitList, name='unit_list'),
    url(r'^UnitCreate/', views.UnitCreate, name='unit_create'),
    url(r'^OldKcsCreate/', views.OldKcsCreate, name='OldKcs_create'),
    url(r'^receive/', views.OldKcsList, name='oldkcs_receive'),
    url(r'^home/', views.home, name='home'),
    url(r'^', views.home, name='home'),
]
