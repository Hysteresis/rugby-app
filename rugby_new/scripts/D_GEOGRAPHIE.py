from rugby_new.settings import DATA_DIR
import os
import pandas as pd
from app.models import D_Geographie


from rugby_new.settings import DATA_DIR
import os
import pandas as pd
from app.models import D_Geographie


def run():
    D_Geographie.objects.all().delete()

    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
    df = pd.read_csv(csv_file_path, sep=';', dtype=str)

    # Retirer les lignes avec "NR - Non réparti"
    df = df[df['Statut géo'] != 'NR - Non réparti']

    # Retirer les colonnes avec "NR"
    df = df.replace('NR', pd.NA)

    # Filtrer les données pour ne conserver que celles de la région "Auvergne-Rhône-Alpes"
    df = df[df['Région'] == 'Auvergne-Rhône-Alpes']

    # Utiliser un dictionnaire pour garder une trace des enregistrements uniques
    unique_records = {}

    for index, row in df.iterrows():
        record_key = (
            row['Code Commune'],
            row['Code QPV']
        )

        # Vérifier si la clé existe déjà dans le dictionnaire des enregistrements uniques
        if record_key in unique_records:
            # Si la clé existe déjà, passer à l'itération suivante
            continue

        # Si la clé n'existe pas, ajouter l'enregistrement au dictionnaire des enregistrements uniques
        unique_records[record_key] = True

        # Créer l'objet D_Geographie et l'ajouter à la base de données
        geographie_obj = D_Geographie(
            code_commune=row['Code Commune'],
            code_qpv=row['Code QPV'],
            commune=row['Commune'],
            qpv=row['Nom QPV'],
            departement=row['Département'],
            region=row['Région'],
            status_geo=row['Statut géo']
        )
        geographie_obj.save()

    print("L'insertion des lignes est terminée.")