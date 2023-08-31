from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()

router.register(r'posts', views.PostViewSet,)
router.register(r'groups', views.GroupViewSet,)
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    views.CommentViewSet,
    basename='comments',
)
router.register(r'follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls),),
]
