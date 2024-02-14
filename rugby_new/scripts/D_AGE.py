from app.models import ODS_lic, D_Age


def run():
    D_Age.objects.all().delete()

    # ce script fonctionne mais je vais regarder en json pour le sexe
    # tranches_age = []
    #
    # for field_name in ODS_lic._meta.fields:
    #     if 'f_' in field_name.name or 'h_' in field_name.name:
    #         parts = field_name.name.split('_')
    #         age_range = '_'.join(part for part in parts if part and any(char.isdigit() for char in part))
    #         if age_range and age_range not in tranches_age:
    #             tranches_age.append(age_range)
    #
    # # Insérer les tranches d'âge dans la table D_Age
    # for age_range in tranches_age:
    #     print(age_range)
    #     D_Age.objects.create(pk_age=age_range)


