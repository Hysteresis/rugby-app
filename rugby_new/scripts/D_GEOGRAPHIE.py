from rugby_new.settings import DATA_DIR
import os
import pandas as pd
from app.models import D_Geographie


from rugby_new.settings import DATA_DIR
import os
import pandas as pd
from app.models import D_Geographie


def insert_geography_data_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path, sep=';', dtype=str)
    df = df.dropna(subset=['Code Commune'])
    df = df[df['Code Commune'] != 'NR - Non réparti']
    df = df[df['Code QPV'] != 'NR - Non réparti']
    df = df[df['Région'] == 'Auvergne-Rhône-Alpes']

    for index, row in df.iterrows():
        geography_obj, created = D_Geographie.objects.get_or_create(
            code_commune=row['Code Commune'],
            code_qpv=row['Code QPV'],
            defaults={
                'commune': row['Commune'],
                'qpv': row['Nom QPV'],
                'departement': row['Département'],
                # 'nom_departement': row['Département'],
                'region': row['Région'],
                'status_geo': row['Statut géo']
            }
        )
        if not created:
            # Si l'objet existait déjà, mettez à jour les autres champs si nécessaire
            geography_obj.commune = row['Commune']
            geography_obj.qpv = row['Nom QPV']
            geography_obj.departement = row['Département']
            # geography_obj.nom_departement = row['nom_departement']
            geography_obj.region = row['Région']
            geography_obj.status_geo = row['Statut géo']
            geography_obj.save()

        print(f"Géographie {geography_obj.code_commune}-{geography_obj.code_qpv}: {geography_obj.commune}")


def run():
    D_Geographie.objects.all().delete()

    csv_files = ['clubs-data-2021.csv', 'lic-data-2021.csv'] # Liste de vos fichiers CSV contenant les données de géographie
    for csv_file in csv_files:
        csv_file_path = os.path.join(DATA_DIR, csv_file)
        insert_geography_data_from_csv(csv_file_path)

# def run():
#     D_Geographie.objects.all().delete()
#
#     csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
#     df = pd.read_csv(csv_file_path, sep=';', dtype=str)
#     df = df.dropna(subset=['Code Commune'])
#     df = df[df['Code Commune'] != 'NR - Non réparti']
#     df = df[df['Région'] == 'Auvergne-Rhône-Alpes']
#
#     unique_records = {}
#
#     for index, row in df.iterrows():
#         if row['Code Commune'] == 'NR - Non réparti':
#             continue
#         record_key = (
#             row['Code Commune'],
#             row['Code QPV']
#         )
#
#         if record_key in unique_records:
#             continue
#
#         unique_records[record_key] = True
#
#         geographie_obj = D_Geographie(
#             code_commune=row['Code Commune'],
#             code_qpv=row['Code QPV'],
#             commune=row['Commune'],
#             qpv=row['Nom QPV'],
#             departement=row['Département'],
#             region=row['Région'],
#             status_geo=row['Statut géo']
#         )
#         geographie_obj.save()
#     print("Bulk geographie")
