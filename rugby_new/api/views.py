# import django_filters
from datetime import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from app.models import F_Club, D_Federation, D_Geographie, D_Date, City
from app import serializers
from app.serializers import FClubSerializer, DFederationSerializer, DDateSerializer, CitySerializer
from rest_framework.pagination import PageNumberPagination
from django.db import transaction
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter

# Create your views here.


class FClubPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EndPointClub(APIView):
    """Here my first API
    get arg:
    - table
    """
    def get(self, request):
        clubs = F_Club.objects.all()
        num_clubs = clubs.count()

        federations = D_Federation.objects.all()
        num_federations = federations.count()
        print(num_federations)

        geographies = D_Geographie.objects.all()
        num_geographies = geographies.count()

        serializer = FClubSerializer(clubs, many=True)
        data = {
            'num_clubs': num_clubs,
            'num_federations': num_federations,
            'num_geographies': num_geographies,
            'clubs': serializer.data
        }

        return Response(data)



        # def post(self, request):
        #     data = request.data
        #     result = {
        #         'message': 'POST a fonctionné',
        #         'data': data
        #     }
        #     return Response(result, status=status.HTTP_201_CREATED)


class Date_api(APIView):
    # http:// 127.0.0.1:8000/api/dates/?date = 2021-01-01
    def get(self, request):
        date_param = request.query_params.get('date', None)
        if date_param:
            try:
                date = datetime.strptime(date_param, '%Y-%m-%d').date()
                dates = D_Date.objects.filter(pk_date=date)
                serializer = DDateSerializer(dates, many=True)
                return Response(serializer.data)
            except ValueError:
                return Response({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)
        else:
            dates = D_Date.objects.all()
            serializer = DDateSerializer(dates, many=True)
            return Response(serializer.data)

    # http_method_names = ['psot']

    def post(self, request):
        try:
            date_data = request.data.get('pk_date')

            if not date_data:
                return Response({"message": "Veuillez fournir une date"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = DDateSerializer(data={'pk_date': date_data})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class City_api(APIView):
    def get(self, request):
        name = request.query_params.get('name', None)
        if name:
            cities = City.objects.filter(name__icontains=name)
        else:
            cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        data = {
            'Ville': serializer.data,
        }
        return Response(data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

