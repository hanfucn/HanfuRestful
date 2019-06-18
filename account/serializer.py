'''

Copyright (C) 2019 张珏敏.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

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
