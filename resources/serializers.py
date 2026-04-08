from rest_framework import serializers
from .models import Recurs, Tag, Autor


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
        
        def validate(self, data):
            if not data.get("nom"):
                raise serializers.ValidationError({
            "nom": "El nom no pot estar buit"
        })
            return data


class RecursSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    autor = serializers.StringRelatedField()

    # 🔥 PER ESCRIURE (assignar autor des del frontend)
    autor = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(),
        required=False,
        allow_null=True
    )

    # 🔥 PER MOSTRAR NOM
    autor_nom = serializers.StringRelatedField(
        source='autor',
        read_only=True
    )

    class Meta:
        model = Recurs
        fields = "__all__"
        
        def validate(self, data):
            if not data.get("titol"):
                raise serializers.ValidationError({
                "titol": "El títol no pot estar buit"
            })
            return data