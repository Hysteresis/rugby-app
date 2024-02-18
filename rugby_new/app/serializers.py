from rest_framework import serializers
from app.models import F_Club, D_Federation


class FClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_Club
        fields = '__all__'


class DFederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_Federation
        fields = '__all__'

