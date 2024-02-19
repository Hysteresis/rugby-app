import os
from datetime import datetime

import pandas as pd
from app.models import D_Type, D_Date, D_Federation, D_Geographie, F_Club
from rugby_new.settings import DATA_DIR


def run():
    pass
    # D_Type.objects.all().delete()
    # D_Date.objects.all().delete()
    #
    # # D_Type
    # types = ["Clubs", "EPA"]
    # instances = [D_Type(pk_type=type) for type in types]
    # D_Type.objects.bulk_create(instances)
    # print("Bulk type")
    #
    #
    # # D_Date
    # chemin_fichier_csv = "data/clubs-data-2021.csv"
    # nom_fichier = os.path.basename(chemin_fichier_csv)
    # annee_str = nom_fichier.split('-')[2].split('.')[0]
    # print(annee_str)
    # annee = int(annee_str)
    # nouvelle_date = D_Date(pk_date=datetime(annee, 1, 1))
    # nouvelle_date.save()
    # print("Bulk date")


