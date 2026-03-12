from rest_framework import serializers
from datetime import date
from .models import Recurs, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class RecursSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)

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

    def validate_titol(self, value):

        if len(value) < 3:
            raise serializers.ValidationError(
                "El títol ha de tenir almenys 3 caràcters"
            )

        return value

    def validate_data_publicacio(self, value):

        if value and value > date.today():
            raise serializers.ValidationError(
                "La data no pot ser futura"
            )

        return value