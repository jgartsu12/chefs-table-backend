from rest_framework import serializers

from posts.models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'phlog_title', 'phlog_description', 'phlog_image_url', 'phlog_status', 'position')