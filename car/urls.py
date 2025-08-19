# car/urls.py
from django.urls import path
from .views import CarListCreateAPIView, CarDetailView, CarUpdateView, CarDeleteView
from . import views

urlpatterns = [
    path('carscreate/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/detail/', CarDetailView.as_view(), name='car-detail'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    
    
    path('', views.car_list, name='car_list'),
    path('create/', views.car_create, name='car_create'),
    path('<int:pk>/', views.car_details, name='car_details'),
    path('<int:pk>/update/', views.car_update, name='car_update'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
]
