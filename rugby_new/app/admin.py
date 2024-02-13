from django.contrib import admin
from app.models import Player, ODS, ODS_lic

# Register your models here.
admin.site.register(Player)
admin.site.register(ODS)
admin.site.register(ODS_lic)
