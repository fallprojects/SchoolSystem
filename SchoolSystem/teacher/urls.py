from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register',RegisterLoginView)

urlpatterns = [
    path('teacher/<int:pk>/',TeacherView.as_view(),name='teacher'),
    path('subjects/<int:pk>/',PupilstoSubjects.as_view(),name='subjects'),
    path('sub/pupils/<int:pupil_id>/',PupilSUbjectDetailGrade.as_view()),
    path('register/', include(router.urls), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
]


