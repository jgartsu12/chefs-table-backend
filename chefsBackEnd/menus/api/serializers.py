from rest_framework import serializers

from menus.models import Menus

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ('id', 'title')