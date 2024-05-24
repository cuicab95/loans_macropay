from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'external_id',
            'icon',
            'key_menu',
            'link',
            'order_menu',
            'parent_id',
            'title',
            'type_menu',
        )



