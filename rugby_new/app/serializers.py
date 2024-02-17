from rest_framework import serializers
from app.models import F_Club


class FClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_Club
        fields = '__all__'

