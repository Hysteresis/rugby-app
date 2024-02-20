from rest_framework import serializers
from app.models import F_Club, D_Federation, D_Date, City, D_Geographie


class FClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_Club
        fields = '__all__'


class DFederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_Federation
        fields = '__all__'


class DDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_Date
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class D_GeographieSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_Geographie
        fields = '__all__'
