import os
from app.models import ODS
import pandas as pd
from rugby_new.settings import DATA_DIR


def run():
    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
    df = pd.read_csv(csv_file_path, sep=';')
    df = df[df['Code Commune'] != 'NR - Non réparti']
    df = df[df['Code QPV'] != 'NR - Non réparti']
    df = df[df['Région'] == 'Auvergne-Rhône-Alpes']

    ODS.objects.all().delete()
    ods_objects = []
    for index, row in df.iterrows():
        ods = ODS(
            code_commune=row['Code Commune'],
            commune=row['Commune'],
            code_qpv=row['Code QPV'],
            nom_qpv=row['Nom QPV'],
            departement=row['Département'],
            region=row['Région'],
            statut_geo=row['Statut géo'],
            code=row['Code'],
            federation=row['Fédération'],
            clubs=row['Clubs'],
            epa=row['EPA'],
        )
        ods_objects.append(ods)
    ODS.objects.bulk_create(ods_objects)

