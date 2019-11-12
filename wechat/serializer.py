from rest_framework import serializers
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature

from wechat import models
from hanfurestful import settings


class WexinAccessSerializers(serializers.Serializer):
    '''
    微信服务器来源验证
    '''
    signature = serializers.CharField(max_length=100, help_text='签名')
    timestamp = serializers.IntegerField(help_text='时间戳')
    nonce = serializers.CharField(max_length=100, help_text='')
    echostr = serializers.CharField(max_length=20, help_text='微信随机字符串', read_only=True, allow_null=True,
                                    allow_blank=True, required=False)

    def validate(self, attrs):
        context_token = settings.WEI_XIN.get('APP_TOKEN')
        context_signature = attrs.get('signature')
        context_timestamp = attrs.get('timestamp')
        context_nonce = attrs.get('nonce')

        print('校验')

        try:
            check_signature(context_token, context_signature, context_timestamp, context_nonce)
        except InvalidSignatureException:
            raise serializers.ValidationError("密匙不匹配哦！")

        return attrs


class WeixinAccessTokenSerializer(serializers.ModelSerializer):
    '''
    access_token是公众号的全局唯一接口调用凭据，公众号调用各接口时都需使用access_token
    access_token的有效期目前为2个小时，需定时刷新，重复获取将导致上次获取的access_token失效。
    '''

    class Meta:
        model = models.WeixinAccessToken
        fields = '__all__'

    pass


class UserWeiXinListSerializers(serializers.ModelSerializer):
    '''
    微信用户
    '''

    class Meta:
        model = models.UserWeiXin
        fields = '__all__'


class UserWeiXinSerializers(UserWeiXinListSerializers):
    '''
    微信用户
    '''
    pass
