from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('teacher/<int:pk>/',TeacherView.as_view(),name='teacher'),
    path('subjects/<int:pk>/',PupilstoSubjects.as_view(),name='subjects'),
    path('sub/<int:subject_id>/pupils/<int:pupil_id>/',PupilSUbjectDetailGrade.as_view())

]


