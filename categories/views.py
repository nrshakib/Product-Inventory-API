from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from categories.models import CategoryModel
from categories.serializers import CategorySerializer
from utils.api_response import api_response

class CategoryViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def get_object(self):
        lookup_value = self.kwargs.get('pk')

        if lookup_value.isdigit():
           category = get_object_or_404(self.get_queryset(), id=lookup_value)

        else:
           category = get_object_or_404(self.get_queryset(), slug=lookup_value)

        self.check_object_permissions(self.request, category)

        return category

    def list(self, request, *args, **kwargs):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)

        return api_response(
            message= "Categories Retrieved Successfully",
            data= serializer.data,
            status_code= status.HTTP_200_OK
        )

    def create(self,request, *args, **kwargs):
        incoming_data = request.data
        serializer = self.get_serializer(data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Category Created Successfully",
            status_code= status.HTTP_201_CREATED,
            data= serializer.data
        )

    def retrieve(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category)

        return api_response(
            message= "Category Retrieved Successfully",
            status_code= status.HTTP_200_OK,
            data= serializer.data
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        incoming_data = request.data
        serializer = self.get_serializer(instance, data=incoming_data, partial=partial)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Category Updated Successfully",
            status_code= status.HTTP_200_OK,
            data= serializer.data
        )

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()

        return api_response(
            message= "Category Deleted Successfully",
            status_code= status.HTTP_200_OK,
            data= None
        )