import os
from datetime import datetime
from app.models import D_Date


def inserer_date():
    chemin_fichier_csv = "data/clubs-data-2021.csv"
    nom_fichier = os.path.basename(chemin_fichier_csv)
    annee_str = nom_fichier.split('-')[2].split('.')[0]
    annee = int(annee_str)
    nouvelle_date, _ = D_Date.objects.get_or_create(pk_date=datetime(annee, 1, 1).date())
    print("Date insérée dans la base de données :", nouvelle_date.pk_date)


