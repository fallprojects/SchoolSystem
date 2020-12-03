from django.shortcuts import render
from pupils.models import Pupils
from pupils.serializers import PupilsSerializer
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

    def post(self,request,*args,**kwargs):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

class PupilstoSubjects(APIView):
    def get(self,*args,**kwargs):
        subjects = PupilstoObjects.objects.get(id=kwargs['pk'])
        serializer = PupilstoSubjectsSerializer(subjects)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PupilSUbjectDetailGrade(APIView):


    def get(self,*args,**kwargs):
        subjects = PupilstoObjects.objects.get(id=kwargs['subject_id'])
        pupil = Pupils.objects.get(id=kwargs['pupil_id'])
        serializer = PupilsSerializer(pupil)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PupilsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



