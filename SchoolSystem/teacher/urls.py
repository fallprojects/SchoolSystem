from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('teacher/<int:pk>/',TeacherView.as_view(),name='teacher'),
    path('subjects/',PupilstoSubjects.as_view(),name='subjects'),

]


