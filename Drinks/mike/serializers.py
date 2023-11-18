from rest_framework import serializers
from .models import MyName

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyName
        fields = ['id', 'name', 'surname', 'alive']