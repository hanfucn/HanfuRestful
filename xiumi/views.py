# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from hanfurestful import settings
from xiumi import serializer, models
from xiumi.request_mixin import AccessTokenMixin


class AccessTokenViewSet(viewsets.ModelViewSet, AccessTokenMixin):
    '''
    获取access_token的接口
    '''
    serializer_class = serializer.AccessTokenSerializer
    queryset = models.AccessToken.objects.filter()

    def dispatch(self, request, *args, **kwargs):
        self.nonce = self.get_nonce()
        self.app_id = settings.APP_ID
        self.secret = settings.SECRET
        self.token = settings.TOKEN
        return super(AccessTokenViewSet, self).dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.re_get())
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SomePathForArticles(viewsets.ModelViewSet, AccessTokenMixin):
    serializer_class = serializer.AccessTokenSerializer
    queryset = models.AccessToken.objects.filter()

    pass
