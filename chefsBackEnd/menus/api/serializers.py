from rest_framework import serializers

from menus.models import FoodMenus
from menus.models import SoupMenu

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenus
        fields = ('id', 'title', 'name', 'description', 'prices')

class SoupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoupMenu
        fields = ('id', 'soup_name', 'soup_prices', 'soup_sizes', 'soup_description')