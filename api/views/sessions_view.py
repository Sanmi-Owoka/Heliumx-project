from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Session
from authentication.permissions import IsITsupport
from ..serializers.sessions_serializer import CreateSessionSerializer, GetSessionSerializer, UpdateSessionSerializer
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import User
from django.http import HttpResponseRedirect
from authentication.utils import Util


class CreateSessionView(generics.GenericAPIView):
    permission_classes = [IsITsupport]
    serializer_class = CreateSessionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        doctor_email = serializer.validated_data['doctor_email']
        patient_email = serializer.validated_data['patient_email_email']
        doctor = User.objects.get(email=doctor_email)
        if not doctor.is_doctor:
            return Response({
                "message": "failed",
                "error": "user is not a doctor",
                "data": "null"
            }, status=status.HTTP_400_BAD_REQUEST)

        patient = User.objects.get(email=patient_email)
        if not patient.is_patient:
            return Response({
                "message": "failed",
                "error": "user is not a patient",
                "data": "null"
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        email_body = 'Hello you have been booked for session with  doctor' + doctor.firstname + '\nmeeting link: ' + \
                     serializer.validated_data['meeting_link'] + '\non ' \
                     + serializer.validated_data['schedule_date'].strftime("%d %B, %Y") + \
                     '\nby ' + serializer.validated_data['schedule_time'].strftime("%I%p")

        data = {'email_body': email_body, 'to_email': patient.email, 'email_subject': 'Meeting session'}
        Util.send_email(data)
        email_content = 'Hello you have been booked for session with ' + patient.firstname + '\n meeting link: ' + \
                        serializer.validated_data['meeting_link'] + '\non ' + serializer.validated_data[
                            'schedule_date'].strftime("%d %B, %Y") + \
                        '\nby ' + serializer.validated_data['schedule_time'].strftime("%I%p")

        meet = {'email_body': email_content, 'to_email': doctor.email, 'email_subject': 'Meeting session'}
        Util.send_email(meet)

        return Response({
            'message': 'session successfully created',
            'data': serializer.data,
            'error': 'null'
        }, status=status.HTTP_201_CREATED)


class GenerateMeetingLink(generics.GenericAPIView):
    permission_classes = [IsITsupport]
    serializer_class = CreateSessionSerializer

    def get(self, request):
        return HttpResponseRedirect(redirect_to="http://meet.google.com/new")


class ConfirmSession(generics.GenericAPIView):
    permission_classes = [IsITsupport]
    serializer_class = GetSessionSerializer

    def put(self, request, pk):
        try:
            session = Session.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "Session with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        session.confirm = True
        session.save()
        serializer = self.serializer_class(session)
        return Response({
            'message': 'session has been confirmed',
            'data': serializer.data,
            'error': "null"
        }, status=status.HTTP_200_OK)


class DeleteSessionView(generics.GenericAPIView):
    permission_classes = [IsITsupport]
    serializer_class = CreateSessionSerializer

    def delete(self, request, pk):
        try:
            session = Session.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "session with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        session.delete()
        return Response({
            'message': 'session successfully deleted',
            'data': 'null',
            'errors': 'null'
        }, status=status.HTTP_204_NO_CONTENT)


class UpdateSessionView(generics.GenericAPIView):
    permission_classes = [IsITsupport]
    serializer_class = CreateSessionSerializer

    def put(self, request, pk):
        try:
            session = Session.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            );
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            );
        doctor_email = serializer.validated_data['doctor_email']
        patient_email = serializer.validated_data['patient_email_email']
        try:
            doctor = User.objects.get(email=doctor_email)
        except ObjectDoesNotExist:
            return Response({
                "message": "failed",
                "error": "user is not a doctor",
                "data": "null"
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            patient = User.objects.get(email=patient_email)
        except ObjectDoesNotExist:
            return Response({
                "message": "failed",
                "error": "user is not a patient",
                "data": "null"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        email_body = 'Hello you have been booked for session with  doctor' + doctor.firstname + '\nmeeting link: ' + \
                     serializer.validated_data['meeting_link'] + '\non ' \
                     + serializer.validated_data['schedule_date'].strftime("%d %B, %Y") + \
                     '\nby ' + serializer.validated_data['schedule_time'].strftime("%I%p")

        data = {'email_body': email_body, 'to_email': patient.email, 'email_subject': 'Meeting session'}
        Util.send_email(data)
        email_content = 'Hello you have been booked for session with ' + patient.firstname + '\n meeting link: ' + \
                        serializer.validated_data['meeting_link'] + '\non ' + serializer.validated_data[
                            'schedule_date'].strftime("%d %B, %Y") + \
                        '\nby ' + serializer.validated_data['schedule_time'].strftime("%I%p")

        meet = {'email_body': email_content, 'to_email': doctor.email, 'email_subject': 'Meeting session'}
        Util.send_email(meet)
