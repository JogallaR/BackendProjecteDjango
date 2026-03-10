from rest_framework import viewsets
from .models import Recurs, Tag
from .serializers import RecursSerializer, TagSerializer

class RecursViewSet(viewsets.ModelViewSet):
    queryset = Recurs.objects.all()
    serializer_class = RecursSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer