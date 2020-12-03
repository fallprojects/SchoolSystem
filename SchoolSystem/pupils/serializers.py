from .views import *
from rest_framework import serializers
from teacher.models import Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id','subject','grade','date_created']


class PupilsSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True)
    class Meta:
        model = Pupils
        fields = ['id','classes','first_name','last_name','grades']

    def create(self, validated_data):
        grade_data = validated_data.pop('grade')
        Grade.objects.create(**grade_data)

class ClassSerializer(serializers.ModelSerializer):
    pupils = PupilsSerializer(many=True)
    class Meta:
        model = Class
        fields = ['pupil_class','pupils']




