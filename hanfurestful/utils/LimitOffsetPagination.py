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

from collections import OrderedDict
from rest_framework import pagination
from rest_framework.response import Response

from hanfurestful import settings


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
