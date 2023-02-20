from rest_framework import serializers

from reviews.models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
