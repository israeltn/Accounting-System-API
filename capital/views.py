from rest_framework import viewsets, serializers, pagination, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Capital, Overhead
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class OverheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overhead
        fields = '__all__'


class CapitalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]   
    pagination_class = CustomPagination
    queryset = Capital.objects.order_by('-date')
    serializer_class = CapitalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['code', 'title', 'date']  # Specify fields to filter on
    search_fields = ['title', 'amount', 'date', 'code']  # Specify fields to search on

    @action(detail=False, methods=['GET'])
    def all_capital_requests(self, request):
        # Custom logic for GET method with search and filtering
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

    @action(detail=False, methods=['POST'])
    def custom_post(self, request):
        # Custom logic for POST method
        # Example: Create a new Capital object with supporting documents
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Handle supporting documents
        capital_instance = serializer.instance
        supporting_documents = request.FILES.getlist('supporting_documents')
        for document in supporting_documents:
            capital_instance.supporting_documents.create(file=document)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def custom_update(self, request, pk=None):
        # Custom logic for PUT/PATCH method
        # Example: Update a specific Capital object
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Handle supporting documents
        supporting_documents = request.FILES.getlist('supporting_documents')
        if supporting_documents:
            # Delete existing supporting documents
            instance.supporting_documents.all().delete()

            # Create new supporting documents
            for document in supporting_documents:
                instance.supporting_documents.create(file=document)
        else:
            # No supporting documents uploaded, delete existing ones
            instance.supporting_documents.all().delete()

        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def custom_delete(self, request, pk=None):
        # Custom logic for DELETE method
        # Example: Delete a specific Capital object
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)




class OverheadViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]    
    
    pagination_class = CustomPagination
    queryset = Overhead.objects.order_by('-date')
    serializer_class = OverheadSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['code', 'title', 'date']  # Specify fields to filter on
    search_fields = ['title', 'amount', 'date', 'code']  # Specify fields to search on

    @action(detail=False, methods=['GET'])
    def all_overhead_requests(self, request):
        # Custom logic for GET method with search and filtering
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


    @action(detail=False, methods=['POST'])
    def custom_post(self, request):
        # Custom logic for POST method
        # Example: Create a new Overhead object with supporting documents
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Handle supporting documents
        Overhead_instance = serializer.instance
        supporting_documents = request.FILES.getlist('supporting_documents')
        for document in supporting_documents:
            Overhead_instance.supporting_documents.create(file=document)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def custom_update(self, request, pk=None):
        # Custom logic for PUT/PATCH method
        # Example: Update a specific Overhead object
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Handle supporting documents
        supporting_documents = request.FILES.getlist('supporting_documents')
        if supporting_documents:
            # Delete existing supporting documents
            instance.supporting_documents.all().delete()

            # Create new supporting documents
            for document in supporting_documents:
                instance.supporting_documents.create(file=document)
        else:
            # No supporting documents uploaded, delete existing ones
            instance.supporting_documents.all().delete()

        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def custom_delete(self, request, pk=None):
        # Custom logic for DELETE method
        # Example: Delete a specific Overhead object
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)





class CommercialViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Overhead.objects.all()
    serializer_class = OverheadSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['GET'])
    def all_capital_requests(self, request):
        # Custom logic for GET method
        # Example: Return a list of all Capital objects       
      queryset = Overhead.objects.order_by('-date')
      page = self.paginate_queryset(queryset)
      if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

      serializer = self.get_serializer(queryset, many=True)
      return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def custom_post(self, request):
        # Custom logic for POST method
        # Example: Create a new Overhead object with supporting documents
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Handle supporting documents
        Overhead_instance = serializer.instance
        supporting_documents = request.FILES.getlist('supporting_documents')
        for document in supporting_documents:
            Overhead_instance.supporting_documents.create(file=document)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def custom_update(self, request, pk=None):
        # Custom logic for PUT/PATCH method
        # Example: Update a specific Overhead object
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Handle supporting documents
        supporting_documents = request.FILES.getlist('supporting_documents')
        if supporting_documents:
            # Delete existing supporting documents
            instance.supporting_documents.all().delete()

            # Create new supporting documents
            for document in supporting_documents:
                instance.supporting_documents.create(file=document)
        else:
            # No supporting documents uploaded, delete existing ones
            instance.supporting_documents.all().delete()

        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def custom_delete(self, request, pk=None):
        # Custom logic for DELETE method
        # Example: Delete a specific Overhead object
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
