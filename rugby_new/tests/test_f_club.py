from django.test import TestCase
from app.models import F_Club

class TestFClubModel(TestCase):
    def setUp(self):
        self.f_club = F_Club.objects.create(
            code="2021-01-01_74315-CSZ_249_EPA",
            fk_date="2021-01-01",
            fk_geographie="74315-CSZ - Yvoire - nan - 74 - - Auvergne-Rhône-Alpes - 1.Champ geoc",
            fk_federation="FF de Sauvetage et de Secourisme",
            fk_type="EPA",
            nombre=0
        )

    def test_f_club_code(self):
        self.assertEqual(self.f_club.code, "2021-01-01_74315-CSZ_249_EPA")
