from rest_framework import serializers
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'email', 'username', 'password']
        pass
