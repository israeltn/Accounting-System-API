from rest_framework import viewsets, pagination, status
from rest_framework.response import Response
from .models import Capital, station, Cheeck
from rest_framework.decorators import action
from .serializers import (
    CapitalSerializer
) 

# Create your views here.
class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CapitalViewSet(viewsets.ModelViewSet):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['GET'])
    def custom_get(self, request):
        # Custom logic for GET method
        # Example: Return a list of all Capital objects
        queryset = self.get_queryset()
        paginator = self.get_paginator()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(page, many=True)
        return Response({
            'status': True,
            'data': {
                'results': serializer.data,  # Paginated data
                'count': paginator.page.paginator.count,
                'page': paginator.page.number,
                'page_size': paginator.page_size,
            },
            'message': 'Capital retrieved successfully.'
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def custom_post(self, request):
        # Custom logic for POST method
        # Example: Create a new Capital object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def custom_update(self, request, pk=None):
        # Custom logic for PUT/PATCH method
        # Example: Update a specific Capital object
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def custom_delete(self, request, pk=None):
        # Custom logic for DELETE method
        # Example: Delete a specific Capital object
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)