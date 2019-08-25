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

from rest_framework import serializers

from . import models


class ArticleSerializer(serializers.ModelSerializer):
    '''
    序列化文章模型
    '''
    image = serializers.SerializerMethodField(help_text='论坛文章 Image List')

    def get_image(self, instance):
        request = self.context.get('request', None)
        return ArticleImageSerializer(instance.articleimage_set, many=True, context={'request': request}).data

    class Meta:
        model = models.Article
        fields = '__all__'

    pass


class ArticleImageSerializer(serializers.ModelSerializer):
    '''
    论坛文章 Image List
    '''

    class Meta:
        model = models.ArticleImage
        fields = '__all__'

    pass
