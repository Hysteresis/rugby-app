from django.contrib import admin
from app.models import Player, ODS, ODS_lic, D_Date, D_Age

# Register your models here.
admin.site.register(Player)
admin.site.register(ODS)
admin.site.register(ODS_lic)
admin.site.register(D_Date)
admin.site.register(D_Age)