from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from categories.models import CategoryModel
from categories.serializers import CategorySerializer

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