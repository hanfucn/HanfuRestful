from collections import OrderedDict
from rest_framework import pagination
from rest_framework.response import Response

from huaxiaRestful import settings


class Pagination(pagination.LimitOffsetPagination):
    """
    自定义分页方法
    """
    page_size_query_param = "page_size"
    page_query_param = 'page'
    page_size = settings.PAGE_SIZE_LIMIT
    default_limit = settings.DEFAULT_LIMIT

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))

    pass


class PaginationObject(pagination.LimitOffsetPagination):
    """
    自定义分页方法
    """
    page_size_query_param = "page_size"
    page_query_param = 'page'
    page_size = settings.PAGE_SIZE_LIMIT
    default_limit = settings.DEFAULT_LIMIT

    def get_paginated_response(self, data):
        return OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ])

    pass
