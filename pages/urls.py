from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeIndex, name='home'),
]