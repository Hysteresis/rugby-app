from app.models import ODS_lic, D_Age


def run():
    tranches_age = []

    for field_name in ODS_lic._meta.fields:
        if 'f_' in field_name.name or 'h_' in field_name.name:
            parts = field_name.name.split('_')
            age_range = '_'.join(part for part in parts if any(char.isdigit() for char in part))
            if age_range not in tranches_age:
                tranches_age.append(age_range)

    # Insérer les tranches d'âge dans la table D_Age
    for age_range in tranches_age:
        D_Age.objects.create(pk_age=age_range)

