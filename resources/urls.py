from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecursViewSet, TagViewSet

router = DefaultRouter()
router.register("recursos", RecursViewSet)
router.register("tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]