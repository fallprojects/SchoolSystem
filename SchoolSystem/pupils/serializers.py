from .views import *
from rest_framework import serializers

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class PupilsSerializer(serializers.ModelSerializer):
    classes = ClassSerializer()
    class Meta:
        model = Pupils
        fields = '__all__'
