from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Newletter
from authentication.permissions import IsCommunityManager
from ..serializers.newletter_serializer import CreateNewletter, GetNewletter, UpdateNewletter
from authentication.models import User
from django.core.exceptions import ObjectDoesNotExist


class NewletterView(generics.GenericAPIView):
    permission_classes = [IsCommunityManager]
    serializer_class = CreateNewletter

    def post(self, request):
        user = User.objects.get(email=request.user.email)
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        newletter = Newletter.objects.create(
            user=user,
            title=serializer.validated_data['title'],
            content=serializer.validated_data['content']
        )
        newletter.save()
        return Response({
            'message': 'Newsletter created successfully',
            'data': serializer.data,
            'errors': 'null'
        }, status=status.HTTP_201_CREATED)


class GetNewLetterView(generics.GenericAPIView):
    permission_classes = [IsCommunityManager]
    serializer_class = GetNewletter

    def get(self, request):
        newletter = Newletter.objects.all()
        serializer = self.serializer_class(newletter, many=True)
        return Response({
            'message': 'Newsletter gotten successfully',
            'data': serializer.data,
            'errors': 'null'
        }, status=status.HTTP_200_OK)


class UpdateNewletterView(generics.GenericAPIView):
    permission_classes = [IsCommunityManager]
    serializer_class = UpdateNewletter

    def patch(self, request, pk):
        try:
            newsletter = Newletter.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(newsletter, data=request.data, partial=True)
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

    def delete(self, request, pk):
        try:
            newsletter = Newletter.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "newsletter with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        newsletter.delete()
        return Response({
            'message': 'newsletter successfully deleted',
            'data': 'null',
            'errors': 'null'
        }, status=status.HTTP_204_NO_CONTENT)
