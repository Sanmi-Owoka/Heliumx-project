from rest_framework import serializers
from ..models import User


class AssignAdminRole(serializers.ModelSerializer):
    roles = serializers.ChoiceField(choices=['user', 'community manager', 'accountant', 'IT support'])

    class Meta:
        model = User
        fields = ['roles']
