from django.db import models


class Autor(models.Model):
    nom = models.CharField(max_length=100)
    cognoms = models.CharField(max_length=150, blank=True)
    nacionalitat = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nom} {self.cognoms}".strip()


class Recurs(models.Model):

    class Meta:
        verbose_name = "Recurs"
        verbose_name_plural = "Recursos"

    class Categoria(models.TextChoices):
        LLIBRE = 'LL', 'Llibre'
        VIDEO = 'VI', 'Vídeo'
        CURS = 'CU', 'Curs'

    titol = models.CharField(max_length=200, unique=True)
    descripcio = models.TextField(blank=True)

    categoria = models.CharField(
        max_length=2,
        choices=Categoria.choices,
        default=Categoria.LLIBRE
    )

    data_publicacio = models.DateField()

    is_active = models.BooleanField(default=True)

    # 🔥 RELACIÓ (1 autor per recurs)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='recursos',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titol


class Tag(models.Model):

    recurs = models.ForeignKey(
        Recurs,
        on_delete=models.CASCADE,
        related_name='tags'
    )

    nom = models.CharField(max_length=50)

    class Meta:
        unique_together = ['recurs', 'nom']

    def __str__(self):
        return self.nom