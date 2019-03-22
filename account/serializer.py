import time

from rest_framework import serializers
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    '''
    用户注册序列化
    API： authorization-register
    '''
    class Meta:
        model = models.User
        fields = ['id', 'email', 'username', 'password']
        pass


class UserSerializer(serializers.ModelSerializer):
    '''
    用户信息序列化
    '''

    date_joined = serializers.SerializerMethodField()

    def get_date_joined(self, instance):
        if instance.last_login: return int(time.mktime(instance.last_login.now().timetuple()))
        return None

    class Meta:
        model = models.User
        fields = ['id', 'email', 'username', 'is_staff', 'date_joined']
