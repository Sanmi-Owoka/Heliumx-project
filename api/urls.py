from django.urls import path
from .views.newletter_view import NewletterView, GetNewLetterView, UpdateNewletterView, DeleteNewsletter
from .views.subscription_view import CreateSubscriptionView, GetSubscriptionView, UpdateSubscriptionView, \
    DeleteSubscriptionView
from .views.sessions_view import CreateSessionView, GenerateMeetingLink, ConfirmSession, DeleteSessionView, \
    UpdateSessionView

urlpatterns = [
    path("newsletter/create", NewletterView.as_view(), name='create newsletter'),
    path("newsletter/get", GetNewLetterView.as_view(), name='get newsletter'),
    path("newsletter/delete/<int:pk>", DeleteNewsletter.as_view(), name="delete newsletter"),
    path("newsletter/update/<int:pk>", UpdateNewletterView.as_view(), name='update newsletter'),
    path("subscription/create", CreateSubscriptionView.as_view(), name='create subscription'),
    path("subscription/get", GetSubscriptionView.as_view(), name='get subscription'),
    path("subscription/update/<int:pk>", UpdateSubscriptionView.as_view(), name='update subscription'),
    path("subscription/delete/<int:pk>", DeleteSubscriptionView.as_view(), name="delete subscription"),
    path("session/create", CreateSessionView.as_view(), name='create session'),
    path("session/generateMeeetingLink", GenerateMeetingLink.as_view(), name='generate link'),
    path("session/confirm/<int:pk>", ConfirmSession.as_view(), name='confirm session'),
    path("session/delete/<int:pk>", DeleteSessionView.as_view(), name="delete session"),
    path("session/update/<int:pk>", UpdateSessionView.as_view(), name="update session")
]
