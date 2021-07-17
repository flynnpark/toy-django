from core.users.views import UserViewSet
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter(trailing_slash=False)
else:
    router = SimpleRouter(trailing_slash=False)

router.register(r'/users', UserViewSet)

app_name = 'v1'

urlpatterns = router.urls
