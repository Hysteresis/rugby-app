import os
from datetime import datetime

import pandas as pd
from app.models import D_Type, D_Date, D_Federation, D_Geographie
from rugby_new.settings import DATA_DIR


def run():
    # D_Type
    D_Type.objects.all().delete()

    types = ["Club", "EPA"]
    instances = [D_Type(pk_type=type) for type in types]
    print(instances)
    D_Type.objects.bulk_create(instances)

    # D_Date
    D_Date.objects.all().delete()

    chemin_fichier_csv = "data/clubs-data-2021.csv"
    nom_fichier = os.path.basename(chemin_fichier_csv)
    annee_str = nom_fichier.split('-')[2].split('.')[0]
    print(annee_str)
    annee = int(annee_str)
    nouvelle_date = D_Date(pk_date=datetime(annee, 1, 1))
    nouvelle_date.save()

# D_Federation
    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
    df = pd.read_csv(csv_file_path, sep=';', dtype=str)
    print(df.head())

    for index, row in df.iterrows():
        federation_obj, created = D_Federation.objects.get_or_create(
            pk_federation=row['Code'],
            defaults={'federation': row['Fédération']}
        )

    print(f"Fédération {federation_obj.pk_federation}: {federation_obj.federation}")


    # D_Geographie
    D_Geographie.objects.all().delete()

    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
    df = pd.read_csv(csv_file_path, sep=';', dtype=str)
    df_filtered = df[
        ~((df == 'NR') | (df == 'NR - Non réparti') | (df == '3.NR')).any(axis=1)
    ]

    print(df_filtered.head())

    geographie_objects = []
    seen_records = set()

    for index, row in df_filtered.iterrows():
        record_key = (
            row['Code Commune'],
            row['Code QPV'],
            row['Commune'],
            row['Nom QPV'],
            row['Département'],
            row['Région'],
            row['Statut géo']
        )

        if record_key in seen_records:
            continue
        seen_records.add(record_key)

        geographie_obj = D_Geographie(
            code_commune=row['Code Commune'],
            code_qpv=row['Code QPV'],
            commune=row['Commune'],
            qpv=row['Nom QPV'],
            departement=row['Département'],
            region=row['Région'],
            status_geo=row['Statut géo']
        )
        geographie_objects.append(geographie_obj)

    D_Geographie.objects.bulk_create(geographie_objects)

    # D_
