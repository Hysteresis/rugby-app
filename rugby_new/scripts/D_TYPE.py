import os
import pandas as pd
from app.models import D_Type
from rugby_new.settings import DATA_DIR


def run():
    D_Type.objects.all().delete()

    types = ["Clubs", "EPA"]
    instances = [D_Type(pk_type=type) for type in types]
    print(instances)
    D_Type.objects.bulk_create(instances)
