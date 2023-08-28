from rest_framework.routers import DefaultRouter, Route


class NoDetailRouter(DefaultRouter):
    """
    A router with only list action.
    """
    routes = [
        # List route
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
    ]
