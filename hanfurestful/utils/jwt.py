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
from rest_framework_jwt.utils import jwt_payload_handler

from account.serializer import UserSerializer


def jwt_payload_handlers(user):
    '''
    自定义Token JWT handlers 信息
    :param user:
    :return:
    '''
    payload = jwt_payload_handler(user)

    last_login = user.last_login
    if last_login: last_login = int(time.mktime(user.last_login.now().timetuple()))

    payload.update({
        'pk': user.pk,
        'username': user.username,
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'last_login': last_login,
    })
    return payload


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    # print('timeArray', user.last_login.now())
    # t = int(time.mktime(user.last_login.now().timetuple()))
    # print('timeArray', datetime.datetime.fromtimestamp(t))
    last_login = user.last_login
    if last_login: last_login = int(time.mktime(user.last_login.now().timetuple()))

    return {
        'user': UserSerializer(user).data,
        'token': token,
    }

def jwt_get_username_from_payload_handler(payload):
    """
    Override this function if username is formatted differently in payload
    """
    print('user', payload)
    return payload.get('username')