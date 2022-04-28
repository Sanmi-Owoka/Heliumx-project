from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Session
from authentication.permissions import IsITsupport
from ..serializers.sessions_serializer import CreateSessionSerializer, GetSessionSerializer
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import User
from rest_framework.permissions import AllowAny
from django.http import HttpResponseRedirect


class CreateSessionView(generics.GenericAPIView):
    permission_classes = [IsITsupport]
    serializer_class = CreateSessionSerializer

    def post(self, request):
        doctor_email = request.data.get('doctor_email', '')
        patient_email = request.data.get('patient_email', '')
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
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
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
