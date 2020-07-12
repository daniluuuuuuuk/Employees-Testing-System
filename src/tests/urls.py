from django.urls import path
from . import views


urlpatterns = [
    path('', views.tests, name='tests'),
    path('questions/', views.questions, name='questions'),
]
