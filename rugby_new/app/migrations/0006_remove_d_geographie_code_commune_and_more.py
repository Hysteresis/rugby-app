# Generated by Django 5.0.2 on 2024-02-17 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_d_age_d_date_d_federation_d_geographie_d_sexe_d_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='d_geographie',
            name='code_commune',
        ),
        migrations.RemoveField(
            model_name='d_geographie',
            name='code_qpv',
        ),
    ]