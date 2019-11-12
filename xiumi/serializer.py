import urllib

import requests
from django.core.files import File
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from xiumi import models


class PartnerUserSerializer(serializers.ModelSerializer):
    '''
    用户登录入口
    '''

    class Meta:
        model = models.PartnerUser
        fields = '__all__'


class AccessTokenSerializer(serializers.ModelSerializer):
    '''
    获取access_token的接口
    '''

    class Meta:
        model = models.AccessToken
        fields = '__all__'

    pass


class SomeArticlesSerializer(serializers.ModelSerializer):
    '''
    接收图文内容的接口
    '''

    class Meta:
        model = models.SomeArticles
        fields = '__all__'

    pass


class SomePathForArticlesSerializer(WritableNestedModelSerializer):
    '''
    接收图文内容的接口
    '''

    articles = SomeArticlesSerializer(many=True, help_text='接收的图文内容 子级')

    class Meta:
        model = models.SomePathForArticles
        fields = '__all__'

    pass


class SomePathForImageDataSerializer(serializers.ModelSerializer):
    """
    接收图片文件 子级
    """

    class Meta:
        model = models.SomePathForImageData
        fields = '__all__'

    pass


class SomePathForImageSerializer(WritableNestedModelSerializer):
    """
    接收图片文件 父级
    """
    data = SomePathForImageDataSerializer()

    class Meta:
        model = models.SomePathForImage
        fields = '__all__'

    pass
