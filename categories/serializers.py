from rest_framework import serializers

from categories.models import CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    
    class Meta:
        model = CategoryModel
        fields = '__all__'