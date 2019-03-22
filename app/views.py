from django.shortcuts import render
from rest_framework import viewsets

from huaxiaRestful.utils.LimitOffsetPagination import Pagination
from . import serializer, models


# Create your views here.

class ArticleView(viewsets.ModelViewSet):
    pagination_class = Pagination
    serializer_class = serializer.ArticleSerializer
    queryset = models.Article.objects.filter()
    filterset_fields = ['name', 'text', 'verify', 'browse', 'user']
    pass
