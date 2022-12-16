from rest_framework import serializers
from .models import Item, Firm, Category


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'