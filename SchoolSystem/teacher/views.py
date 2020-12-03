from django.shortcuts import render
from pupils.models import Pupils
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

class TeacherView(APIView):
    def get(self,*args,**kwargs):
        teacher = Teacher.objects.get(id=kwargs['pk'])
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PupilstoSubjects(APIView):
    def get(self,*args,**kwargs):
        subjects = PupilstoObjects.objects.all()
        serializer = PupilstoSubjectsSerializer(subjects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

