from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
from api.routers import NoDetailRouter


router = DefaultRouter()
no_detail_router = NoDetailRouter()

router.register(r'posts', views.PostViewSet,)
router.register(r'groups', views.GroupViewSet,)
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    views.CommentViewSet,
    basename='comments',
)
no_detail_router.register(r'follow', views.FollowViewSet, basename='follow')
print(router.urls)
print()
print(no_detail_router.urls)

urlpatterns = [
#    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls),),
    path('', include(no_detail_router.urls),),
]
