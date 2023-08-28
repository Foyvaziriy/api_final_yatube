from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Comment, Group, Follow


class FollowSerilizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    following = serializers.CharField()

    class Meta:
        model = Follow
        fields = ('user', 'following',)
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',)
            ),
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)
        read_only_fields = ('id', 'title', 'slug', 'description',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, many=False,)
    comments = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date', 'author', 'image', 'group', 'comments',
        )
        read_only_fields = ('id', 'pub_date,' 'author', 'comments',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('id', 'author', 'post', 'created',)
