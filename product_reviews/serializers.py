from rest_framework import serializers
from .models import Review

#Class Serializer

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_text', 'rating', 'name', 'product_id']