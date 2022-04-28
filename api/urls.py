from django.urls import path
from .views.newletter_view import NewletterView, GetNewLetterView
from .views.subscription_view import CreateSubscriptionView, GetSubscriptionView, UpdateSubscriptionView
urlpatterns = [
    path("newsletter/create", NewletterView.as_view(), name='create newsletter'),
    path("newsletter/get", GetNewLetterView.as_view(), name='get newsletter'),
    path("subscription/create", CreateSubscriptionView.as_view(), name='create subscription'),
    path("subscription/get", GetSubscriptionView.as_view(), name='get subscription'),
    path("subscription/update/<int:pk>", UpdateSubscriptionView.as_view(), name='update subscription')
]