from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecursViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'recursos', RecursViewSet)
router.register(r'autors', AutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]