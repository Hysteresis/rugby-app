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
    ODS des clubs
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

    def count_columns(cls):
        return len(cls._meta.fields)


class ODS_lic(models.Model):
    """
    ODS des licenciés
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
    f_1_4_ans = models.CharField(max_length=255, default='0')
    f_5_9_ans = models.CharField(max_length=255, default='0')
    f_10_14_ans = models.CharField(max_length=255, default='0')
    f_15_19_ans = models.CharField(max_length=255, default='0')
    f_20_24_ans = models.CharField(max_length=255, default='0')
    f_25_29_ans = models.CharField(max_length=255, default='0')
    f_30_34_ans = models.CharField(max_length=255, default='0')
    f_35_39_ans = models.CharField(max_length=255, default='0')
    f_40_44_ans = models.CharField(max_length=255, default='0')
    f_45_49_ans = models.CharField(max_length=255, default='0')
    f_50_54_ans = models.CharField(max_length=255, default='0')
    f_55_59_ans = models.CharField(max_length=255, default='0')
    f_60_64_ans = models.CharField(max_length=255, default='0')
    f_65_69_ans = models.CharField(max_length=255, default='0')
    f_70_74_ans = models.CharField(max_length=255, default='0')
    f_75_79_ans = models.CharField(max_length=255, default='0')
    f_80_99_ans = models.CharField(max_length=255, default='0')
    f_nr = models.CharField(max_length=255, default='0')
    h_1_4_ans = models.CharField(max_length=255, default='0')
    h_5_9_ans = models.CharField(max_length=255, default='0')
    h_10_14_ans = models.CharField(max_length=255, default='0')
    h_15_19_ans = models.CharField(max_length=255, default='0')
    h_20_24_ans = models.CharField(max_length=255, default='0')
    h_25_29_ans = models.CharField(max_length=255, default='0')
    h_30_34_ans = models.CharField(max_length=255, default='0')
    h_35_39_ans = models.CharField(max_length=255, default='0')
    h_40_44_ans = models.CharField(max_length=255, default='0')
    h_45_49_ans = models.CharField(max_length=255, default='0')
    h_50_54_ans = models.CharField(max_length=255, default='0')
    h_55_59_ans = models.CharField(max_length=255, default='0')
    h_60_64_ans = models.CharField(max_length=255, default='0')
    h_65_69_ans = models.CharField(max_length=255, default='0')
    h_70_74_ans = models.CharField(max_length=255, default='0')
    h_75_79_ans = models.CharField(max_length=255, default='0')
    h_80_99_ans = models.CharField(max_length=255, default='0')
    h_nr = models.CharField(max_length=255, default='0')
    nr_nr = models.CharField(max_length=255, default='0')
    total = models.CharField(max_length=255, default='0')
    # date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.commune} - {self.departement} - {self.f_1_4_ans}"


class D_Date(models.Model):
    pk_date = models.DateField(primary_key=True)


    def __str__(self):
        return str(self.pk_date)


class D_Age(models.Model):
    pk_age = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.pk_age


class D_Sexe(models.Model):
    pk_sexe = models.CharField(max_length=1, primary_key=True)
    label = models.CharField(max_length=50)
    def __str__(self):
        return self.label


class D_Federation(models.Model):
    pk_federation = models.CharField(max_length=5, primary_key=True)
    federation = models.CharField(max_length=255)

    def __str__(self):
        return self.federation


class D_Type(models.Model):
    pk_type = models.CharField(max_length=5, primary_key=True)

    def __str__(self):
        return self.pk_type


class D_Geographie(models.Model):
    pk_geographie = models.CharField(max_length=90, primary_key=True)
    # code_commune = models.CharField(max_length=30)
    # code_qpv = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    qpv = models.CharField(max_length=255)
    departement = models.CharField(max_length=50)
    nom_departement = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    status_geo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pk_geographie} - {self.commune} - {self.qpv} - {self.departement} - {self.nom_departement} - {self.region} - {self.status_geo}"


class F_Club(models.Model):
    code = models.CharField(max_length=255, primary_key=True)
    fk_date = models.ForeignKey(D_Date, on_delete=models.CASCADE)
    fk_geographie = models.ForeignKey(D_Geographie, on_delete=models.CASCADE)
    fk_federation = models.ForeignKey(D_Federation, on_delete=models.CASCADE)
    fk_type = models.ForeignKey(D_Type, on_delete=models.CASCADE)
    nombre = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.nombre}"



# class F_Licence(models.Model):
#     pk_licence = models.CharField(max_length=255, primary_key=True)
#
#     def __str__(self):
#         # return self.
#         pass



