import os
from datetime import date

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from api.views import City_api
import json

from app.models import F_Club, D_Federation, D_Date, D_Sexe, D_Geographie, D_Age, D_Type, ODS, City
from rugby_new import settings


factory = APIRequestFactory()
request = factory.delete('cities/63000/')
view = City_api.as_view()

response = view(request, postal_code='63000')
response.render()
json_response = json.loads(response.content)


class TestCityApi(TestCase):
    def setUp(self):
        pass

    def test_delete_city(self):
        self.assertEqual(response.status_code, 204)



