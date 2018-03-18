from django.urls import path, include
from rest_framework import routers
from api_v0 import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientListViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list),
    path('view/', include(router.urls)),
    path('clients/<int:pk>/', views.client_detail),
]