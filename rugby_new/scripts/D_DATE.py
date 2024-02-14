import os
from datetime import datetime
from app.models import D_Date


def run():
    chemin_fichier_csv = "data/clubs-data-2021.csv"
    nom_fichier = os.path.basename(chemin_fichier_csv)
    annee_str = nom_fichier.split('-')[2].split('.')[0]
    print(annee_str)
    annee = int(annee_str)
    nouvelle_date = D_Date(pk_date=datetime(annee, 1, 1))
    # print(nouvelle_date)
    # nouvelle_date.save()

