import os
from datetime import datetime

import pandas as pd
from app.models import D_Type, D_Date, D_Federation, D_Geographie, F_Club
from rugby_new.settings import DATA_DIR


def run():
    D_Type.objects.all().delete()
    D_Date.objects.all().delete()

    # D_Type
    types = ["Club", "EPA"]
    instances = [D_Type(pk_type=type) for type in types]
    D_Type.objects.bulk_create(instances)
    print("Bulk type")


    # D_Date
    chemin_fichier_csv = "data/clubs-data-2021.csv"
    nom_fichier = os.path.basename(chemin_fichier_csv)
    annee_str = nom_fichier.split('-')[2].split('.')[0]
    print(annee_str)
    annee = int(annee_str)
    nouvelle_date = D_Date(pk_date=datetime(annee, 1, 1))
    nouvelle_date.save()
    print("Bulk date")


    # D_Federation

    # D_Geographie


    # # F_Club
    F_Club.objects.all().delete()

    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')

    df = pd.read_csv(csv_file_path, sep=';', dtype=str, na_values=['NR - Non réparti', 'NR'])

    df = df[df['Région'] == 'Auvergne-Rhône-Alpes']

    date_obj, created_date = D_Date.objects.get_or_create(pk_date=datetime(2021, 1, 1))

    clubs_to_create = []

    existing_clubs = set()

    for index, row in df.iterrows():
        geographie_obj, created_geo = D_Geographie.objects.get_or_create(code_commune=row['Code Commune'],
                                                                         code_qpv=row['Code QPV'],
                                                                         defaults={'commune': row['Commune'],
                                                                                   'qpv': row['Nom QPV'],
                                                                                   'departement': row['Département'],
                                                                                   'region': row['Région'],
                                                                                   'status_geo': row['Statut géo']})
        federation_obj, created_fed = D_Federation.objects.get_or_create(pk_federation=row['Code'],
                                                                         defaults={'federation': row['Fédération']})
        type_value = 'EPA' if row.get('EPA') else 'Club'
        type_obj, created_type = D_Type.objects.get_or_create(pk_type=type_value, defaults={'type': type_value})

        # Vérifier si une instance avec les mêmes clés étrangères existe déjà
        club_key = (date_obj.pk, geographie_obj.pk, federation_obj.pk, type_obj.pk)
        if club_key in existing_clubs:
            # print("Doublon trouvé")
            continue

        existing_clubs.add(club_key)


        # Licence: 4023594
        # Club: 31674
        # "table_name": "D_Federation",        "count": 101,
        # "table_name": "D_Geography",        "count": 4172,
        # Créer l'instance de F_Club uniquement si les données ne sont pas manquantes
        if not pd.isna(row['Clubs']):
            club = F_Club(
                fk_date=date_obj,
                fk_geographie=geographie_obj,
                fk_federation=federation_obj,
                fk_type=type_obj,
                nombre=row['Clubs']
            )

            clubs_to_create.append(club)

            if len(clubs_to_create) == 10000:
                F_Club.objects.bulk_create(clubs_to_create)
                clubs_to_create = []

    if clubs_to_create:
        F_Club.objects.bulk_create(clubs_to_create)

    print("Bulk F_Clubs OK")
