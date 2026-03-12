from django.db import models

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

    data_publicacio = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

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