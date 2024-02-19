import os

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from api.views import City_api
import json

from app.models import F_Club, D_Federation, D_Date, D_Sexe, D_Geographie, D_Age, D_Type, ODS, City
from rugby_new import settings
from scripts.ETL_ODS import run

# Create your tests here.

factory = APIRequestFactory()
request = factory.get('cities/75001/')
view = City_api.as_view()
response = view(request, postal_code='75001')
response.render()
json_response = json.loads(response.content)


class TestCities(TestCase):
    # python manage.py test
    def setUp(self):
        pass

    def test_type(self):
        record = {
                    "postal_code": "75001",
                    "name": "Paris",
                    "department": "Paris",
                    "region": "Île-de-France",
                    "country": "France"
        }

        self.assertEqual(json_response[0], record)

    def test_create_city(self):
        new_city_data = {
            "postal_code": "75003",
            "name": "Paris 3",
            "department": "Paris",
            "region": "Île-de-France",
            "country": "France"
        }
        request = factory.post('/cities/', new_city_data, format='json')
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['postal_code'], new_city_data['postal_code'])
        self.assertEqual(response.data['name'], new_city_data['name'])
        self.assertEqual(response.data['department'], new_city_data['department'])
        self.assertEqual(response.data['region'], new_city_data['region'])
        self.assertEqual(response.data['country'], new_city_data['country'])

    def test_create_city_invalid_data(self):
        invalid_city_data = {
            "postal_code": "75003",
            "department": "Paris",
            "region": "Île-de-France",
            "country": "France"
        }
        request = factory.post('/cities/', invalid_city_data, format='json')
        response = view(request)

        # Assurez-vous que la réponse contient un statut HTTP 400 BAD REQUEST
        self.assertEqual(response.status_code, 400)

    def test_patch_city(self):
        existing_city = City.objects.create(
                postal_code="63000",
                name="Clermont",
                department="Puy-de-Dôme",
                region="Auvergne-Rhône-Alpes",
                country="France"
        )
        valid_city_data = {
            "name": "Clermont-Ferrand",
        }
        request = factory.patch('/cities/75001/', valid_city_data)
        response = view(request, postal_code='63000')
        self.assertEqual(response.status_code, 200)

class TestFClubModel(TestCase):
    def setUp(self):
        # Créer une instance de F_club pour le test
        date_instance = D_Date.objects.create(pk_date="2021-01-01")
        geographie_instance = D_Geographie.objects.create(
            pk_geographie="74315-CSZ - Yvoire - nan - 74 - - Auvergne-Rhône-Alpes - 1.Champ geoc",
            commune="Yvoire",
            qpv="...",
            departement="74",
            nom_departement="Auvergne-Rhône-Alpes",
            region="...",
            status_geo="..."
        )
        federation_instance = D_Federation.objects.create(
            pk_federation="123",
            federation="FF de Sauvetage"
        )
        type_instance = D_Type.objects.create(
            pk_type="EPA"
        )
        self.f_club = F_Club.objects.create(
            code="2021-01-01_74315-CSZ_249_EPA",
            fk_date=date_instance,
            fk_geographie=geographie_instance,
            fk_federation=federation_instance,
            fk_type=type_instance,
            nombre=0
        )

    def test_f_club_code(self):
        self.assertEqual(self.f_club.code, "2021-01-01_74315-CSZ_249_EPA")
        self.assertEqual(self.f_club.fk_date.pk_date, "2021-01-01")
        self.assertEqual(self.f_club.fk_geographie.commune, "Yvoire")
        self.assertEqual(self.f_club.fk_federation.federation, "FF de Sauvetage")
        self.assertEqual(self.f_club.fk_type.pk_type, "EPA")
        self.assertEqual(self.f_club.nombre, 0)

    def test_number_of_instances(self):
        expected_total_f_clubs = 1
        total_f_clubs = F_Club.objects.count()
        self.assertEqual(total_f_clubs, expected_total_f_clubs)

    def test_update_f_club_nombre(self):
        self.f_club.nombre = 10
        self.f_club.save()
        updated_f_club = F_Club.objects.get(code="2021-01-01_74315-CSZ_249_EPA")

        self.assertEqual(updated_f_club.nombre, 10)


class TestETLClub(TestCase):
    def setUp(self):
        self.csv_file_path = os.path.join(settings.BASE_DIR, 'test_clubs-data-2021.csv')














#     def setUp(self):
#         self.csv_file_path = os.path.join(settings.BASE_DIR, 'test_clubs-data-2021.csv')
#         with open(self.csv_file_path, 'w') as f:
#             f.write(
#                 """Code Commune;Commune;Code QPV;Nom QPV;Département;Région;Statut géo;Code;Fédération;Clubs;EPA\n
#                 12345;VilleA;QPV123;NomQPV123;DepartementA;Auvergne-Rhône-Alpes;StatutA;ABC;FF Rugby;ClubA;EPA1\n
#                 67890;VilleB;QPV456;NomQPV456;DepartementB;Auvergne-Rhône-Alpes;StatutB;DEF;FF Football;ClubB;EPA2\n"""
#             )
#
#     def tearDown(self):
#         os.remove(self.csv_file_path)
#
#     def test_etl(self):
#         run()
#
#         self.assertEqual(ODS.objects.count(), 15837)
#



