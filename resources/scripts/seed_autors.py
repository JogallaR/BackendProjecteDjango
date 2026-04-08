from resources.models import Autor, Recurs


def run():
    print("Creant dades...")

    autor = Autor.objects.create(
        nom="George",
        cognoms="Orwell"
    )

    Recurs.objects.create(
        titol="1984",
        categoria="LL",
        autor=autor
    )

    print("OK!")