from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('wei', views.WexinAccess, base_name='wei')
router.register('access-token', views.AccessTokenViewSet, base_name='access-token')
router.register('wei-user', views.UserWeiXinViewSet, base_name='wei-user')

urlpatterns = [
    path('', include(router.urls))
]
