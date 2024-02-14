from app.models import ODS_lic, D_Sexe


def run():
    D_Sexe.objects.all().delete()

    sexes = ["H", "F"]
    instances = [D_Sexe(pk_sexe=sexe) for sexe in sexes]
    print(instances)
    D_Sexe.objects.bulk_create(instances)







