from rest_framework.viewsets import (
    ModelViewSet, ReadOnlyModelViewSet, GenericViewSet)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)
from rest_framework import filters, mixins
from django.db.models.query import QuerySet

from posts.models import Post, Comment, Group, Follow
from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerilizer
)
from api.services import get_filtered_objects, get_all_objects
from api.permissions import IsAuthorOrReadOnly


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    serializer_class = FollowSerilizer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet:
        return get_filtered_objects(model=Follow, user=self.request.user)

    def perform_create(self, serializer: FollowSerilizer) -> None:
        serializer.save(user=self.request.user)

    def get_serializer_context(self) -> dict:
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = get_all_objects(model=Group)
    serializer_class = GroupSerializer


class PostViewSet(ModelViewSet):
    queryset = get_all_objects(model=Post)
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer: PostSerializer) -> None:
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)

    def get_queryset(self) -> QuerySet:
        return get_filtered_objects(
            model=Comment, post_id=self.kwargs['post_id'])

    def perform_create(self, serializer: CommentSerializer) -> None:
        serializer.save(
            post_id=self.kwargs['post_id'],
            author=self.request.user,
        )
