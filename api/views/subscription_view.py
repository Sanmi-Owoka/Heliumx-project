from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Subscription
from authentication.permissions import IsAccountant
from ..serializers.subscription_serializer import CreateSubscription, GetSubscription, UpdateSubscription
from django.core.exceptions import ObjectDoesNotExist


class CreateSubscriptionView(generics.GenericAPIView):
    permission_classes = [IsAccountant]
    serializer_class = CreateSubscription

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        subcription = Subscription.objects.create(
            type=serializer.validated_data['type'],
            details=serializer.validated_data['details']
        )
        subcription.save()
        return Response({
            'message': 'subcription successfully created',
            'data': serializer.data,
            'errors': "null"
        }, status=status.HTTP_201_CREATED)


class GetSubscriptionView(generics.GenericAPIView):
    permission_classes = [IsAccountant]
    serializer_class = GetSubscription

    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = self.serializer_class(subscription, many=True)
        return Response({
            'message': "subscription successfully gotten",
            'data': serializer.data,
            'errors': 'null'
        }, status=status.HTTP_200_OK)


class UpdateSubscriptionView(generics.GenericAPIView):
    permission_classes = [IsAccountant]
    serializer_class = UpdateSubscription

    def patch(self, request, pk):
        try:
            subscription = Subscription.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(subscription, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response({
            'message': 'success',
            'data': serializer.data,
            'errors': 'null'
        }, status=status.HTTP_200_OK)
