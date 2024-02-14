import os
from datetime import datetime

from app.models import D_Date
# import pandas as pd
# from rugby_new.settings import DATA_DIR


def run():
    chemin_fichier_csv = "data/clubs-data-2021.csv"
    nom_fichier = os.path.basename(chemin_fichier_csv)
    annee_str = nom_fichier.split('-')[2].split('.')[0]
    annee = int(annee_str)
    nouvelle_date = D_Date(pk_date=datetime(annee, 1, 1))
    print(nouvelle_date)
    nouvelle_date.save()
    # csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
    # df = pd.read_csv(csv_file_path, sep=';')
    # # df = pd.read_csv('data/clubs-data-2021.csv', sep=';')
    # print(df.head())
    # ODS.objects.all().delete()
    # ods_objects = []
    # for index, row in df.iterrows():
    #     ods = ODS(
    #         code_commune=row['Code Commune'],
    #         commune=row['Commune'],
    #         code_qpv=row['Code QPV'],
    #         nom_qpv=row['Nom QPV'],
    #         departement=row['Département'],
    #         region=row['Région'],
    #         statut_geo=row['Statut géo'],
    #         code=row['Code'],
    #         federation=row['Fédération'],
    #         clubs=row['Clubs'],
    #         epa=row['EPA'],
    #     )
    #     ods_objects.append(ods)
    # ODS.objects.bulk_create(ods_objects)

