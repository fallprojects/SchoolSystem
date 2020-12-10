from django.shortcuts import render
from pupils.models import Pupils
from pupils.serializers import PupilsSerializer, GradeSerializer
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework import status, viewsets
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

class TeacherView(APIView):
    def get(self,*args,**kwargs):
        teacher = Teacher.objects.get(id=kwargs['pk'])
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PupilstoSubjects(APIView):
    def get(self,*args,**kwargs):
        subjects = PupilstoObjects.objects.get(id=kwargs['pk'])
        serializer = PupilstoSubjectsSerializer(subjects)
        return Response(serializer.data,status=status.HTTP_200_OK)


class PupilSUbjectDetailGrade(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,*args,**kwargs):

        pupil = Pupils.objects.get(id=kwargs['pupil_id'])
        serializer = PupilsSerializer(pupil)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PupilsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RegisterLoginView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AccountLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request':request}
                                           )
        if not serializer.is_valid():
            return Response({'User not found'})
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})


