import json

from app.models import ODS_lic, D_Sexe


def run():
    D_Sexe.objects.all().delete()

    # with open('mapping/licence_sexe.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)
    # instances = [D_Sexe(pk_sexe=key, sexe_label=value) for key, value in data.items()]
    sexes = ["H", "F"]
    instances = [D_Sexe(pk_sexe=sexe) for sexe in sexes]
    print(instances)
    D_Sexe.objects.bulk_create(instances)







