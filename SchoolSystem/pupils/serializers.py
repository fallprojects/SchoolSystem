from .views import *
from rest_framework import serializers

class PupilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ['id','classes','first_name','last_name','grade']

class ClassSerializer(serializers.ModelSerializer):
    pupils = serializers.StringRelatedField(many=True)
    class Meta:
        model = Class
        fields = ['pupil_class','pupils']
