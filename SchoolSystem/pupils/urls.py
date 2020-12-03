from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('pupils/<int:pk>/',PupilsView.as_view(),name='pupils'),

]



