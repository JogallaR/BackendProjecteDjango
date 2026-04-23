from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from resources.models import Recurs, Autor
from datetime import date


class RecursAPITest(APITestCase):

    def setUp(self):
        self.recurs = Recurs.objects.create(
            titol="Recurs inicial",
            data_publicacio=date.today()
        )

    # -------------------------
    # CREACIÓ
    # -------------------------
    def test_create_recurs_valid(self):
        url = reverse('recurs-list')

        data = {
            "titol": "Nou recurs",
            "data_publicacio": date.today(),
            "categoria": "LL"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_recurs_missing_fields(self):
        url = reverse('recurs-list')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unique_titol(self):
        url = reverse('recurs-list')

        data = {
            "titol": "Recurs inicial",
            "data_publicacio": date.today()
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_categoria(self):
        url = reverse('recurs-list')

        data = {
            "titol": "Categoria incorrecta",
            "data_publicacio": date.today(),
            "categoria": "XX"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_titol_max_length(self):
        url = reverse('recurs-list')

        data = {
            "titol": "A" * 300,  # supera 200
            "data_publicacio": date.today()
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # -------------------------
    # LECTURA
    # -------------------------
    def test_list_recursos(self):
        url = reverse('recurs-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_recurs(self):
        url = reverse('recurs-detail', args=[self.recurs.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_recurs_not_found(self):
        url = reverse('recurs-detail', args=[999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # -------------------------
    # UPDATE
    # -------------------------
    def test_update_recurs_put_valid(self):
        url = reverse('recurs-detail', args=[self.recurs.id])

        data = {
            "titol": "Actualitzat",
            "data_publicacio": date.today(),
            "categoria": "VI"
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_recurs_invalid_categoria(self):
        url = reverse('recurs-detail', args=[self.recurs.id])

        response = self.client.patch(url, {"categoria": "ZZ"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # -------------------------
    # DELETE
    # -------------------------
    def test_delete_recurs(self):
        url = reverse('recurs-detail', args=[self.recurs.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # -------------------------
    # ALTRES
    # -------------------------
    def test_boolean_default(self):
        self.assertTrue(self.recurs.is_active)


class AutorAPITest(APITestCase):

    def setUp(self):
        self.autor = Autor.objects.create(nom="Autor Test")

    # -------------------------
    # CREACIÓ
    # -------------------------
    def test_create_autor_valid(self):
        url = reverse('autor-list')

        data = {"nom": "Nou Autor"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_autor_empty_name(self):
        url = reverse('autor-list')

        data = {"nom": ""}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_autor_name_max_length(self):
        url = reverse('autor-list')

        data = {"nom": "A" * 200}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # -------------------------
    # RELACIÓ
    # -------------------------
    def test_get_recursos_by_autor(self):
        Recurs.objects.create(
            titol="Recurs 1",
            data_publicacio=date.today(),
            autor=self.autor
        )

        Recurs.objects.create(
            titol="Recurs 2",
            data_publicacio=date.today()
        )

        url = reverse('autor-recursos', args=[self.autor.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_autor_without_recursos(self):
        url = reverse('autor-recursos', args=[self.autor.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    # -------------------------
    # CASCADE
    # -------------------------
    def test_delete_autor_cascade(self):
        Recurs.objects.create(
            titol="Recurs amb autor",
            data_publicacio=date.today(),
            autor=self.autor
        )

        self.autor.delete()
        self.assertEqual(Recurs.objects.count(), 0)