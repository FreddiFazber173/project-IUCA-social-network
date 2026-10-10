from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('schedule'), name='academic_index'),
    path('schedule/', views.schedule_view, name='schedule'),
]