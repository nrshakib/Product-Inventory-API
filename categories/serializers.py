from rest_framework import serializers

from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Name cannot be empty or contain only spaces."
            )
        
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must be at least 3 characters long."
            )

        return value

    def validate_description(self, value):
        if value and not value.strip():
            raise serializers.ValidationError(
                "Description cannot contain spaces only"
            )

        return value.strip()

