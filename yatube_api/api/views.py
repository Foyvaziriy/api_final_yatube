from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import exceptions
from django.db.models.query import QuerySet

from posts.models import Post, Comment, Group, Follow
from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerilizer
)


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerilizer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self) -> QuerySet:
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer: FollowSerilizer) -> None:
        if self.request.user == serializer.validated_data['following']:
            raise exceptions.ParseError('You can not follow yourself.')
        print(serializer.validated_data)
        serializer.save(user=self.request.user)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ('get',)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer: PostSerializer) -> None:
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self) -> QuerySet:
        return Comment.objects.filter(post_id=self.kwargs['post_id'],)

    def perform_create(self, serializer: CommentSerializer) -> None:
        serializer.save(
            post_id=self.kwargs['post_id'],
            author=self.request.user,
        )
