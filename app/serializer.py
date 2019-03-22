from rest_framework import serializers

from . import models


class ArticleSerializer(serializers.ModelSerializer):
    '''
    序列化文章模型
    '''
    class Meta:
        model = models.Article
        fields = '__all__'
    pass
