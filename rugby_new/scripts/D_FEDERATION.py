import os
import pandas as pd
from app.models import D_Federation
from rugby_new.settings import DATA_DIR


def run():
    csv_file_path = os.path.join(DATA_DIR, 'lic-data-2021.csv')
    df = pd.read_csv(csv_file_path, sep=';', dtype=str)
    print(df.head())

    for index, row in df.iterrows():
        federation_obj, created = D_Federation.objects.get_or_create(
            pk_federation=row['Code'],
            defaults={'federation': row['Fédération']}
        )

    print(f"Fédération {federation_obj.pk_federation}: {federation_obj.federation}")





