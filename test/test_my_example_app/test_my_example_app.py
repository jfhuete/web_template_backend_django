import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from my_example_app.models import Musician, Album


class AbstractCategoryViewsetTestsCase(APITestCase):

    def setUp(self):
        self.musician1 = Musician.objects.create(
            first_name="first_foo",
            last_name="first_bar",
            instrument="first_baz",
        )
        Musician.objects.create(
            first_name="second_foo",
            last_name="second_bar",
            instrument="second_baz",
        )
        Album.objects.create(
            artist=self.musician1,
            name="album_foo",
            release_date=datetime.date(2022, 10, 19),
            num_stars=5
        )

    def test_list_musicians(self):
        """
        Test response for GET /musician
        """

        url = reverse("musician-list")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_musician(self):
        """
        Test response for GET /musician/:pk
        """

        url = reverse("musician-detail", kwargs={"pk": self.musician1.pk})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.data,
            {
                "id": self.musician1.pk,
                "first_name": "first_foo",
                "last_name": "first_bar",
                "instrument": "first_baz",
            }
        )

    def test_create_musician(self):
        """
        Test response for POST /musician
        """

        musician = {
            "first_name": "create_foo",
            "last_name": "create_bar",
            "instrument": "create_baz",
        }

        url = reverse("musician-list")
        response = self.client.post(url, musician, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        musician_created = response.data

        Musician.objects.get(pk=musician_created["id"])

    def test_full_update_musician(self):
        """
        Test response for PUT /musician/:id
        """

        musician = {
            "first_name": "update_foo",
            "last_name": "update_bar",
            "instrument": "update_baz",
        }

        url = reverse("musician-detail", kwargs={"pk": self.musician1.pk})
        response = self.client.put(url, musician, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        musician_updated = Musician.objects.get(pk=self.musician1.pk)

        self.assertEqual(musician["first_name"], musician_updated.first_name)
        self.assertEqual(musician["last_name"], musician_updated.last_name)
        self.assertEqual(musician["instrument"], musician_updated.instrument)

    def test_partial_update_musician(self):
        """
        Test response for PATCH /musician/:id
        """

        musician = {
            "first_name": "update_foo",
        }

        url = reverse("musician-detail", kwargs={"pk": self.musician1.pk})
        response = self.client.patch(url, musician, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        musician_updated = Musician.objects.get(pk=self.musician1.pk)

        self.assertEqual(musician["first_name"], musician_updated.first_name)
        self.assertEqual(musician_updated.last_name, self.musician1.last_name)
        self.assertEqual(musician_updated.instrument, self.musician1.instrument)

    def test_delete_musician(self):
        """
        Test response for DELETE /musician/:id
        """

        url = reverse("musician-detail", kwargs={"pk": self.musician1.pk})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Musician.objects.count(), 1)
