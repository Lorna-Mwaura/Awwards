from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('image','title','url','detail_desciption','created_date')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic')