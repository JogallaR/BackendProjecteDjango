from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Recurs, Autor
from .serializers import RecursSerializer, AutorSerializer


class RecursViewSet(viewsets.ModelViewSet):
    queryset = Recurs.objects.all()
    serializer_class = RecursSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=True, methods=['get'])
    def recursos(self, request, pk=None):
        autor = self.get_object()
        recursos = Recurs.objects.filter(autor=autor)
        serializer = RecursSerializer(recursos, many=True)
        return Response(serializer.data)