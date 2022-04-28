from rest_framework import serializers
from ..models import User


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        style={"input_type": "email", "placeholder": "Email"},
    )

    class Meta:
        model = User
        fields = ["email", "password"]

        extra_kwargs = {
            "password": {
                "required": True,
                "style": {"input_type": "password", "placeholder": "Password"},
            },
        }
