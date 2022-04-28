from rest_framework import serializers
from ..models import Subscription


class CreateSubscription(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=['basic', 'premium'])
    details = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Subscription
        fields = ['type', 'details']


class GetSubscription(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class UpdateSubscription(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'details']
