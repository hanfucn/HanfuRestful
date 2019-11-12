from __future__ import unicode_literals

import requests
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from wechat import serializer, models
from wechat.viewset import WeiChatEventManagerViewSet


class GenericWeiXin:
    '''
    微信公众号配置部分
    '''

    # 公众号的唯一标识
    app_id = 'wx41e302230d440738'
    app_secret = 'f76448f867921e04fcc1ed5a3bcd98bb'

    server_token = '2ac863cbdd4d18c26e9005514f2ee0ce'
    server_encoding_aes_key = 'U1d4He8Guib3jDYTD5GkndOsPRlp9MF6iWklNsooUgs'

    # 授权后重定向的回调链接地址， 请使用 urlEncode 对链接进行处理
    redirect_uri = ''

    # 返回类型，请填写code
    response_type = 'code'

    '''
    应用授权作用域
    snsapi_base： 不弹出授权页面，直接跳转，只能获取用户openid
    snsapi_userinfo： 弹出授权页面，可通过openid拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息
    '''
    scope = 'snsapi_userinfo'

    # 重定向后会带上state参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
    state = ''

    access_grant_type = 'client_credential'
    access_token = ''
    access_uri = 'https://api.weixin.qq.com/cgi-bin/token?grant_type={grant_type}&appid={appid}&secret={appsecret}'.format(
        appid=app_id,
        appsecret=app_secret,
        grant_type=access_grant_type
    )
    pass


class WexinAccess(WeiChatEventManagerViewSet):
    '''
    微信服务器来源验证
    用来接收微信消息和事件的接口URL
    https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Access_Overview.html
    '''
    serializer_class = serializer.WexinAccessSerializers
    queryset = models.WeixinAccessToken.objects.filter()

    def list(self, request, *args, **kwargs):
        '''
        验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        serializers = serializer.WexinAccessSerializers(data=self.request.query_params)
        serializers.is_valid(raise_exception=True)
        echo_str = self.request.query_params.get('echostr')

        return HttpResponse(echo_str)


class AccessTokenViewSet(ModelViewSet, GenericWeiXin):
    '''
    获取Access token
    https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Get_access_token.html
    '''
    serializer_class = serializer.WeixinAccessTokenSerializer
    queryset = models.WeixinAccessToken.objects.filter()

    def create(self, request, *args, **kwargs):
        response = requests.get(self.access_uri)
        serializer_data = response.json()
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    pass


class UserWeiXinViewSet(ModelViewSet):
    '''
    获取用户信息
    '''
    serializer_class = serializer.UserWeiXinSerializers
    serializer_list_class = serializer.UserWeiXinListSerializers
    queryset = models.UserWeiXin.objects.filter()

    def create(self, request, *args, **kwargs):
        response = requests.get(self.access_uri)
        serializer_data = response.json()
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
