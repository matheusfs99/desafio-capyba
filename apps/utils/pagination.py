from rest_framework import pagination
from rest_framework.pagination import _positive_int
from rest_framework.response import Response
from rest_framework.settings import api_settings


class CustomPagination(pagination.PageNumberPagination):
    default_limit = api_settings.PAGE_SIZE
    limit_query_param = "page_size"
    max_limit = None

    def get_paginated_response(self, data):
        return Response({
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link()
            },
            "total_count": self.page.paginator.count,
            "count_in_page": len(data),
            "results": data
        })

    def get_page_size(self, request):
        if self.limit_query_param:
            try:
                return _positive_int(
                    request.query_params[self.limit_query_param],
                    strict=True,
                    cutoff=self.max_limit
                )
            except (KeyError, ValueError):
                pass

        return self.default_limit
