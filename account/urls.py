from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from rest_framework import routers

from account.views import ObtainJSONWebTokenView, RefreshJSONWebTokenView, VerifyJSONWebTokenView, \
    RegisterUserView

router = routers.DefaultRouter()
router.register('authorization', ObtainJSONWebTokenView, base_name='authorization')
router.register('authorization-register', RegisterUserView, base_name='authorization-register')
router.register('authorization-refresh', RefreshJSONWebTokenView, base_name='authorization-refresh')
router.register('authorization-verify', VerifyJSONWebTokenView, base_name='authorization-verify')

urlpatterns = [
    path('', include(router.urls))
]
