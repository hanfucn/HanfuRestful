"""huaxiaRestful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import mixins, views
from rest_framework.response import Response

from huaxiaRestful import settings

from django.views.static import serve


class AuthIndex(mixins.ListModelMixin, views.APIView):
    '''
    ## auth:
    * auth-token: 获取Token
    * auth-token-refresh: 刷新Token
    * auth-token-verify: 验证Token
    '''

    def get_host_path(self):
        path = '{}{}'.format(self.request.get_host(), self.request.path)
        if self.request.is_secure():
            host = 'https://{}'.format(path)
        else:
            host = 'http://{}'.format(path)
            pass
        return host

    def get_apps(self):
        return settings.INSTALLED_APPS_RESTFUL

    def get(self, request, *args, **kwargs):
        context = {
            'authorization': '{}{}'.format(self.get_host_path(), 'account/authorization/'),
            'authorization-refresh': '{}{}'.format(self.get_host_path(), 'account/authorization-refresh/'),
            'authorization-register': '{}{}'.format(self.get_host_path(), 'account/authorization-register/'),
            'authorization-verify': '{}{}'.format(self.get_host_path(), 'account/authorization-verify/'),
        }
        app = {}

        for item in self.get_apps():
            app.update({
                item: '{}{}/'.format(self.get_host_path(), item),
            })
        return Response({
            'account': context,
            'app': app
        })

    pass


urlpatterns = [
    path('', AuthIndex.as_view(), name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT})
]

'''
自动注册具备RESTFUL支持的APP [INSTALLED_APPS_RESTFUL]
注： 不具备RESTFUL支持的APP需要手动注册
'''
for item in settings.INSTALLED_APPS_RESTFUL:
    urlpatterns.append(
        path('{}/'.format(item), include('{}.urls'.format(item)))
    )
