import os
import pandas as pd
from app.models import D_Federation
from rugby_new.settings import DATA_DIR


def insert_data_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path, sep=';', dtype=str)
    df = df.dropna(subset=['Code Commune'])
    df = df[df['Code Commune'] != 'NR - Non réparti']
    df = df[df['Code QPV'] != 'NR - Non réparti']
    df = df[df['Région'] == 'Auvergne-Rhône-Alpes']

    for index, row in df.iterrows():
        federation_obj, created = D_Federation.objects.get_or_create(
            pk_federation=row['Code'],
            defaults={'federation': row['Fédération']}
        )
        if not created:
            # Si l'objet existait déjà, mettez à jour le nom de la fédération
            federation_obj.federation = row['Fédération']
            federation_obj.save()

        print(f"Fédération {federation_obj.pk_federation}: {federation_obj.federation}")


def run():
    D_Federation.objects.all().delete()

    csv_files = ['clubs-data-2021.csv', 'lic-data-2021.csv']  # Liste de vos fichiers CSV
    for csv_file in csv_files:
        csv_file_path = os.path.join(DATA_DIR, csv_file)
        insert_data_from_csv(csv_file_path)
