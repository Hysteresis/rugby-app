import os

from app.models import Player, ODS
import pandas as pd

from rugby_new.settings import DATA_DIR


def run():
    # lire le fichier CSV
    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
    df = pd.read_csv(csv_file_path, sep=';')
    # df = pd.read_csv('data/clubs-data-2021.csv', sep=';')
    print(df.head())
    ODS.objects.all().delete()
    # test_df = df.head(5)
    # 117390
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
        ods.save()

