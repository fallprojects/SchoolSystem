from .views import *
from rest_framework import serializers

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    classes = ClassSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'

