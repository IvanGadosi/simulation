from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('result/<int:pk>/', views.result_view, name='result')
]