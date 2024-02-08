from django.db import models

# Create your models here.

class Player(models.Model):
    """_summary_
    :arg

    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self,):
        return f"{self.first_name} - {self.last_name}"


class ODS(models.Model):
    """

    """
    code_commune = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    code_qpv = models.CharField(max_length=255)
    nom_qpv = models.CharField(max_length=255)
    departement = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    federation = models.CharField(max_length=255)
    clubs = models.CharField(max_length=255)
    epa = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self,):
        return f"""
            {self.code_commune} - 
            {self.commune} -
            {self.code_qpv} -
            {self.nom_qpv} -
            {self.departement} -
            {self.region} -
            {self.statut_geo} -
            {self.code} -
            {self.federation} -
            {self.clubs} -
            {self.epa} -
            {self.date} -
            
"""
