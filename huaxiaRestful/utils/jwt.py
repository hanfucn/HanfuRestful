import time
from rest_framework_jwt.utils import jwt_payload_handler


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
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'last_login': last_login,
    })
    return payload


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    last_login = user.last_login
    if last_login: last_login = int(time.mktime(user.last_login.now().timetuple()))

    return {
        'user': {
            'pk': user.pk,
            'username': user.username,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'last_login': last_login,
        },
        'token': token,
    }
