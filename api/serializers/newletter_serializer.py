from rest_framework import serializers
from ..models import Newletter


class CreateNewletter(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)
    content = serializers.CharField()

    class Meta:
        model = Newletter
        fields = ['title', 'content']


class GetNewletter(serializers.ModelSerializer):
    class Meta:
        model = Newletter
        fields = '__all__'


class UpdateNewletter(serializers.ModelSerializer):
    class Meta:
        model = Newletter
        fields = ['title', 'content']
