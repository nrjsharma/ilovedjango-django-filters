from rest_framework import serializers
from myapp.models import Post


class ViewPostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %B, %Y", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"