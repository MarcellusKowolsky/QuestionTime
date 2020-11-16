from rest_framework import serializer
from users.models import CustomUser


class UserDisplaySerializer(serializer.ModelSerialzer):
    class Meta:
        model = CustomUser
        fields = ["username"]
