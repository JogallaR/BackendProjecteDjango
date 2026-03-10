from rest_framework import serializers
from .models import Recurs, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class RecursSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # nested

    class Meta:
        model = Recurs
        fields = [
            "id",
            "titol",
            "descripcio",
            "categoria",
            "data_publicacio",
            "is_active",
            "tags",
        ]