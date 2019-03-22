from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('article', views.ArticleView, base_name='article')

urlpatterns = [
    path('', include(router.urls))
]