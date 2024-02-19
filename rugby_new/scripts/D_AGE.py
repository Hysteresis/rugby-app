from app.models import ODS_lic, D_Age


def inserer_age():
    D_Age.objects.all().delete()

    tranches_age = []

    for field_name in ODS_lic._meta.fields:
        if 'f_' in field_name.name or 'h_' in field_name.name:
            parts = field_name.name.split('_')
            age_range = '_'.join(part for part in parts if part and any(char.isdigit() for char in part))
            if age_range and age_range not in tranches_age:
                tranches_age.append(age_range)

    # Créer une liste d'instances D_Age à insérer
    ages_to_create = [D_Age(pk_age=age_range) for age_range in tranches_age]

    # Insérer les tranches d'âge par lot
    batch_size = 1000
    for i in range(0, len(ages_to_create), batch_size):
        D_Age.objects.bulk_create(ages_to_create[i:i + batch_size])



