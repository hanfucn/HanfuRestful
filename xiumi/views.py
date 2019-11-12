# Create your views here.
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from xiumi import serializer, models
from xiumi.base import GenericXiuMiAPIBase


class AccessLoginViewSet(mixins.ListModelMixin, GenericXiuMiAPIBase):
    """
    用户登录入口
    """
    serializer_class = serializer.PartnerUserSerializer
    queryset = models.PartnerUser.objects.filter()

    def list(self, request, *args, **kwargs):
        return Response({
            'uri': self.get_authentication_login_uri()
        })


class AccessTokenViewSet(viewsets.ModelViewSet, GenericXiuMiAPIBase):
    """
    获取access_token的接口
    """
    serializer_class = serializer.AccessTokenSerializer
    queryset = models.AccessToken.objects.filter()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={
            'access_token': self.set_authentication_token_create(),
            'expires_in': 64800
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SomePathForArticlesViewSet(viewsets.ModelViewSet):  # SomePathArticles
    """
    接收图文内容的接口
    """
    serializer_class = serializer.SomePathForArticlesSerializer
    queryset = models.SomePathForArticles.objects.filter()


class SomePathForImageViewSet(viewsets.ModelViewSet):  # SomePathArticles
    """
    接收图片文件的接口
    """
    serializer_class = serializer.SomePathForImageSerializer
    queryset = models.SomePathForImage.objects.filter()
