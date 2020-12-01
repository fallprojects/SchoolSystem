from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('teacher/<int:pk>/',TeacherView.as_view(),name='teacher'),
]
