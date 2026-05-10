#In Django REST Framework (DRF), pagination is used to split large querysets into smaller chunks (pages) so responses are faster and easier to handle.
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'  # optional
    max_page_size = 100