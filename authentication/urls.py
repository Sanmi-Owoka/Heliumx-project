from django.urls import path
from .views.user_views import UserView, UserGetDeleteUpdateView, AddAdminView, AssignAdminRoleView, GetAllUsers, \
    CommunityManagerView, GetAllUsersView
from .views.login_view import LoginView

urlpatterns = [
    path("", UserView.as_view(), name='user view'),
    path("login/", LoginView.as_view(), name='login'),
    path("<int:pk>", UserGetDeleteUpdateView.as_view(), name='update, delete and get'),
    path("get/", GetAllUsersView.as_view(), name='get users'),
    path("admin/add/", AddAdminView.as_view(), name='add admin'),
    path("admin/assignRole/<int:pk>", AssignAdminRoleView.as_view(), name='assign admin role'),
    path("communityManager/<int:pk>", CommunityManagerView.as_view(), name='community manager'),
    path("communityManager/getAllUser/", GetAllUsers.as_view(), name='get all users')
]
