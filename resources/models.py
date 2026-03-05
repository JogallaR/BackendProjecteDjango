from django.db import models

class Recurs(models.Model):

    class Categoria(models.TextChoices):
        LLIBRE = 'LL', 'Llibre'
        VIDEO = 'VI', 'Vídeo'
        CURS = 'CU', 'Curs'

    titol = models.CharField(max_length=200)
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