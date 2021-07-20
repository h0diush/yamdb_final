from django.urls import include, path
from rest_framework.routers import DefaultRouter, Route, SimpleRouter

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet, confirm_email,
                       get_token)


class GenresCategoriesRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={
                'delete': 'destroy',
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]


router = DefaultRouter()
router_genres_categories = GenresCategoriesRouter()
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews', ReviewViewSet, basename='Reviews'
)
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comments'
)
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'users', UserViewSet, basename='users')
router_genres_categories.register(r'genres', GenreViewSet)
router_genres_categories.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('v1/auth/email/', confirm_email, name='confirm_email'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/', include(router_genres_categories.urls))
]
