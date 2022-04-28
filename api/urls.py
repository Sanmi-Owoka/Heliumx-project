from django.urls import path
from .views.newletter_view import NewletterView, GetNewLetterView
from .views.subscription_view import CreateSubscriptionView, GetSubscriptionView, UpdateSubscriptionView
from .views.sessions_view import CreateSessionView, GenerateMeetingLink, ConfirmSession

urlpatterns = [
    path("newsletter/create", NewletterView.as_view(), name='create newsletter'),
    path("newsletter/get", GetNewLetterView.as_view(), name='get newsletter'),
    path("subscription/create", CreateSubscriptionView.as_view(), name='create subscription'),
    path("subscription/get", GetSubscriptionView.as_view(), name='get subscription'),
    path("subscription/update/<int:pk>", UpdateSubscriptionView.as_view(), name='update subscription'),
    path("session/create", CreateSessionView.as_view(), name='create session'),
    path("generateLink", GenerateMeetingLink.as_view(), name='generate link'),
    path("session/confirm/<int:pk>", ConfirmSession.as_view(), name='confirm session')
]
