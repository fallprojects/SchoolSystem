from .views import *
from rest_framework import serializers
from pupils.serializers import ClassSerializer
from django.contrib.auth.models import User

class TeacherSerializer(serializers.ModelSerializer):
    classes = ClassSerializer()
    class Meta:
        model = Teacher
        fields = ['id','last_name','otchestvo','subject','classes']

class PupilstoSubjectsSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(many=True)
    class Meta:
        model = PupilstoObjects
        fields = ['id','subjects','classes']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        password = self.validated_data.get('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
