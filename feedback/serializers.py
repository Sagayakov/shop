from rest_framework import serializers

from .models import FeedbackModel


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FeedbackModel
        fields = '__all__'
