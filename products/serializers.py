from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['slug']

        def validate_name(self,value):
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

        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                    "Price must be greater than zero."
                )
        
            return value

        def validate_stock_quantity(self, value):
            if value < 0:
                raise serializers.ValidationError(
                    "Stock cannot be negative."
                )
                
            return value