from rest_framework import serializers

from phlogfeeder.models import PhlogFeeder

class PhlogFeederSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhlogFeeder
        fields = ('id', 'phlog_title', 'phlog_description', 'phlog_image_url', 'phlog_status' )