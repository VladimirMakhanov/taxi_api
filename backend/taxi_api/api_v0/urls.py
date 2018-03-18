from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api_v0 import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list),
    path('clients/<int:pk>/', views.client_detail),
    path('drivers/', views.driver_list),
    path('drivers/<int:pk>/', views.driver_detail),
    path('cars/', views.car_list),
    path('cars/<int:pk>/', views.car_detail),
    path('tariffs/', views.tariff_list),
    path('tariffs/<int:pk>/', views.tariff_detail),
    path('orders/', views.order_list),
    path('orders/<int:pk>/', views.order_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])