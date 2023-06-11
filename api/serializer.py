from rest_framework import serializers
from myapp.models import Post


class ViewPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"