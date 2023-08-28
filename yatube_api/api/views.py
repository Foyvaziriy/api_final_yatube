from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model

from posts.models import Post, Comment, Group, Follow
from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerilizer
)
from api.exceptions import UndefinedUsernameToFollowError, SelfFollowingError

User = get_user_model()


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerilizer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        username = serializer.validated_data['following']
        try:
            get_object_or_404(User, username=username)
            if username != self.request.user.username:
                serializer.save(user=self.request.user)
            else:
                raise SelfFollowingError
        except Http404:
            raise UndefinedUsernameToFollowError

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except UndefinedUsernameToFollowError:
            return Response(
                {'detail': 'Undefined username.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except SelfFollowingError:
            return Response(
                {'detail': 'You can not follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ('get',)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs['post_id'],
            author=self.request.user
        )
