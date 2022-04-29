from rest_framework import serializers
from ..models import Session


class CreateSessionSerializer(serializers.ModelSerializer):
    doctor_email = serializers.CharField(max_length=255, required=True)
    patient_email = serializers.CharField(max_length=255, required=True)
    meeting_link = serializers.CharField(max_length=255, required=True)
    schedule_date = serializers.DateField()
    schedule_time = serializers.TimeField()

    class Meta:
        model = Session
        fields = ['doctor_email', 'patient_email', 'meeting_link', 'schedule_date', 'schedule_time']


class GetSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class UpdateSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['doctor_email', 'patient_email', 'meeting_link', 'schedule_date', 'schedule_time']
