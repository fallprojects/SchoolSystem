from .views import *
from rest_framework import serializers
from pupils.serializers import *

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


