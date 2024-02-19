import os
from datetime import datetime
from app.models import D_Date, D_Sexe, D_Age, D_Type, D_Federation, D_Geographie
from scripts.D_DATE import inserer_date
from scripts.D_SEXE import inserer_sexe
from scripts.D_AGE import inserer_age
from scripts.D_TYPE import inserer_type
from scripts.D_FEDERATION import inserer_federation
from scripts.D_GEOGRAPHIE import inserer_geographie


def run():
    D_Age.objects.all().delete()
    D_Date.objects.all().delete()
    D_Federation.objects.all().delete()
    D_Sexe.objects.all().delete()
    D_Type.objects.all().delete()
    D_Geographie.objects.all().delete()

    inserer_age()
    inserer_date()
    inserer_federation()
    inserer_sexe()
    inserer_type()
    inserer_geographie()



