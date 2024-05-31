from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class serviceattributeserializer(serializers.ModelSerializer):
    class Meta:
        model = serviceattribute
        fields = '__all__'

class serviceserializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = '__all__'

class skillserializer(serializers.ModelSerializer):
    class Meta:
        model = skill
        fields = '__all__'

class projectserializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class technologyserializer(serializers.ModelSerializer):
    class Meta:
        model = technology
        fields = '__all__'

class docserializer(serializers.ModelSerializer):
    class Meta:
        model = doc
        fields = '__all__'


class socialserializer(serializers.ModelSerializer):
    class Meta:
        model = social
        fields = '__all__'

class edserializer(serializers.ModelSerializer):
    class Meta:
        model = education
        fields = '__all__'
