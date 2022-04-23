from rest_framework import serializers

from cash_register import models

class ListItemSerialiser(serializers.ModelSerializer):
    """Сериализатор списка товаров"""
    class Mete:
        model = models.Item
        fields = ['id', ]