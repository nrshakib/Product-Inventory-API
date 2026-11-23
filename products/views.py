from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer
from utils.api_response import api_response

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        lookup_value = self.kwargs.get('pk')

        if lookup_value.isdigit():
            product = get_object_or_404(self.get_queryset(), id=lookup_value)

        else:
            product = get_object_or_404(self.get_queryset(), slug=lookup_value)

        self.check_object_permissions(self.request, product)

        return product

    def list(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)

        return api_response(
            message= "Products Retrieved Successfully",
            data= serializer.data,
            status_code= status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.get_serializer(product)

        return api_response(
            message= "Product Retrieved Successfully",
            status_code= status.HTTP_200_OK,
            data= serializer.data
        )

    def create(self, request, *args, **kwargs):
        incoming_data = request.data
        serializer = self.get_serializer(data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message = "Product Created Successfully",
            status_code = status.HTTP_201_CREATED,
            data = serializer.data
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        product = self.get_object()
        incoming_data = request.data
        serializer = self.get_serializer(product, data=incoming_data, partial=partial)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Product Updated Successfully",
            status_code= status.HTTP_200_OK,
            data= serializer.data
        )

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()

        return api_response(
            message= "Product Deleted Successfully",
            status_code= status.HTTP_200_OK,
            data= None
        )
