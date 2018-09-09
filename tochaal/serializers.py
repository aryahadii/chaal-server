from rest_framework import serializers
from tochaal.models import Subchaal, Thread, Post


class SubchaalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subchaal
        fields = ('id', 'name', 'created_at', )


class ThreadOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'title', 'created_at', )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'subchaal', 'thread', 'title', 'body', 'created_at', )
