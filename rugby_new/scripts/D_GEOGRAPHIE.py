from rugby_new.settings import DATA_DIR
import os
import pandas as pd
from app.models import D_Geographie


def run():
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

    # Insérer les objets en bloc dans la base de données
    # D_Geographie.objects.bulk_create(geographie_objects, ignore_conflicts=True)
    D_Geographie.objects.bulk_create(geographie_objects)
