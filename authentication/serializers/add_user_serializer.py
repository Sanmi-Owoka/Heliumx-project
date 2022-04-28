from rest_framework import serializers
from ..models import User


class AddUserSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=68, min_length=3, required=True)
    lastname = serializers.CharField(max_length=68, min_length=3, required=True)
    email = serializers.EmailField(max_length=100, min_length=5, required=True)

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email']
