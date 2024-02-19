import os
import sqlite3
from datetime import datetime, date
import pandas as pd
from app.models import F_Club, D_Date, D_Geographie, D_Federation, D_Type
from rugby_new import settings
from rugby_new.settings import DATA_DIR


def run():
    F_Club.objects.all().delete()
    csv_file = 'clubs-data-2021.csv'
    DATA_DIR = os.path.join(settings.BASE_DIR, 'data')

    csv_file_path = os.path.join(DATA_DIR, csv_file)
    df = pd.read_csv(csv_file_path, sep=';', dtype=str)
    df = df[df['Code Commune'] != 'NR - Non réparti']
    df = df[df['Code QPV'] != 'NR - Non réparti']
    df = df[df['Région'] == 'Auvergne-Rhône-Alpes']

    clubs_to_create = []
    i = 0
    # january_2021, created = D_Date.objects.get_or_create(pk_date=date(2021, 1, 1))
    d_date = D_Date.objects.first()
    print(d_date)
    # Créer un ensemble pour stocker les clés des F_Club
    club_keys = set()

    for index, row in df.iterrows():
        pk_geographie = row['Code Commune'] + '-' + row['Code QPV']
        pk_federation = row['Code']

        # Créer la clé pour le club
        club_key = (d_date.pk_date, pk_geographie, pk_federation)

        # Vérifier si le club_key est déjà dans l'ensemble
        if club_key in club_keys:
            print(f"Doublon trouvé pour le club : {club_key}")
        else:
            club_keys.add(club_key)

            try:
                geo = D_Geographie.objects.get(pk_geographie=pk_geographie)
                fede = D_Federation.objects.get(pk_federation=pk_federation)
            except (D_Geographie.DoesNotExist, D_Federation.DoesNotExist) as e:
                print(f"Erreur : {e}")
                continue

            for col in ['Clubs', 'EPA']:
                type_label = col
                alltype, created = D_Type.objects.get_or_create(pk_type=type_label)

                nb_target = int(row[col])

                if alltype:
                    club_code = f"{d_date.pk_date}_{geo.pk_geographie}_{fede.pk_federation}_{alltype.pk_type}"
                    club = F_Club(
                        code=club_code,
                        fk_date=d_date,
                        fk_type=alltype,
                        fk_geographie=geo,
                        fk_federation=fede,
                        nombre=nb_target
                    )
                    print(club)
                    clubs_to_create.append(club)
                else:
                    print(f"Erreur: Type inconnu '{type_label}'")

    F_Club.objects.bulk_create(clubs_to_create)


