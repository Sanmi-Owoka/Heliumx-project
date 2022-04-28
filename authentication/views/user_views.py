from ..serializers.add_user_serializer import AddUserSerializer
from ..serializers.update_user_serializer import UpdateUserSerializer
from ..serializers.add_admin_serializer import AddAdminSerializer
from ..serializers.assign_admin_role import AssignAdminRole
from ..serializers.get_user_serializer import GetUserSerializer
from rest_framework import generics, status
from ..models import User
from rest_framework.response import Response
from ..utils import Util
from ..permissions import IsCEO, IsCommunityManager
from django.core.exceptions import ObjectDoesNotExist


class UserView(generics.GenericAPIView):
    serializer_class = AddUserSerializer
    permission_classes = [IsCEO]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.create(
            firstname=serializer.validated_data['firstname'],
            lastname=serializer.validated_data['lastname'],
            email=serializer.validated_data['email'],
            roles='user',
        )
        password = Util.generate_password(10)
        user.set_password(password)
        user.save()
        return Response({
            'message': 'success',
            'data': serializer.data,
            'password': password,
            'errors': 'null'
        })


class UserGetDeleteUpdateView(generics.GenericAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsCEO]

    def patch(self, request, pk):
        try:
            get_user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(get_user, data=request.data, partial=True)
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
        }, status=status.HTTP_206_PARTIAL_CONTENT)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.delete()
        return Response({
            'message': 'user successfully deleted',
            'data': 'null',
            'errors': 'null'
        }, status=status.HTTP_200_OK)


class AddAdminView(generics.GenericAPIView):
    serializer_class = AddAdminSerializer
    permission_classes = [IsCEO]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.create(
                firstname=serializer.validated_data['firstname'],
                lastname=serializer.validated_data['lastname'],
                email=serializer.validated_data['email'],
                is_admin=True
            )
            password = Util.generate_password(10)
            user.set_password(password)
            user.save()
        except Exception as error:
            return Response({
                'message': "user already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'successfully created admin',
            'data': serializer.data,
            'password': password,
            'errors': 'null'
        }, status=status.HTTP_200_OK)


class AssignAdminRoleView(generics.GenericAPIView):
    serializer_class = AssignAdminRole
    permission_classes = [IsCEO]

    def patch(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not user.is_admin:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "User is not an admin",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(user, data=request.data, partial=True)
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


class CommunityManagerView(generics.GenericAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsCommunityManager]

    def patch(self, request, pk):
        try:
            get_user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(get_user, data=request.data, partial=True)
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

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "failure",
                    "data": "null",
                    "error": "user with does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GetUserSerializer(user)
        return Response({
            'message': 'user successfully gotten',
            'data': serializer.data,
            'errors': 'null'
        }, status=status.HTTP_200_OK)


class GetAllUsers(generics.GenericAPIView):
    permission_classes = [IsCommunityManager]
    serializer_class = GetUserSerializer

    def get(self, request):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response({
            'message': 'users successfully gotten',
            'data': serializer.data,
            'errors': 'null'
        }, status=status.HTTP_200_OK)


