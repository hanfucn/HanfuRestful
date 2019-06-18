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
