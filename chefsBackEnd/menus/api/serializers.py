from rest_framework import serializers

from menus.models import Menus

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ('id', 'titles', 'menu_items', 'menu_items_description', 'soup_prices', 'all_food_but_soups_prices')