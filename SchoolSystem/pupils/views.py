from django.shortcuts import render
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




class PupilsView(APIView):
    def get(self,*args,**kwargs):
        try:
            pupils = Pupils.objects.get(id=kwargs['pk'])
            serializer = PupilsSerializer(pupils)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Pupils.DoesNotExist:
            return Response({"data":"pupil not found"})

