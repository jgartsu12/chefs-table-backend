from rest_framework import serializers

from menus.models import LunchMenu
from menus.models import BreakfastMenu
from menus.models import SoupMenu

class LunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunchMenu
        fields = ('id', 'title', 'name', 'description', 'front_thumb_img_url')

class BreakfastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakfastMenu
        fields = ('id', 'title', 'name', 'description', 'front_thumb_img_url')

class SoupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoupMenu
        fields = ('id', 'title', 'name', 'description', 'front_thumb_img_url')