from rest_framework import serializers

from .models import PhoneModel


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = '__all__'
