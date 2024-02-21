# import django_filters
from datetime import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from app.models import F_Club, D_Federation, D_Geographie, D_Date, City
from app import serializers
from app.serializers import FClubSerializer, DFederationSerializer, DDateSerializer, CitySerializer, \
    D_GeographieSerializer
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
    # http://127.0.0.1:8000/api/
    """Here my first API
    get arg:
    - table
    """
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 4

        clubs = F_Club.objects.all()
        federations = D_Federation.objects.all()
        geographies = D_Geographie.objects.all()

        clubs_page = paginator.paginate_queryset(clubs, request)
        clubs_serializer = FClubSerializer(clubs_page, many=True)

        data = {
            'num_clubs': clubs.count(),
            'num_federations': federations.count(),
            'num_geographies': geographies.count(),
            'clubs': clubs_serializer.data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        }

        return paginator.get_paginated_response(data)



class Date_api(APIView):
    # http://127.0.0.1:8000/api/dates/2021-01-01/
    lookup_field = "pk_date"

    def get(self, request, pk_date=None):
        if pk_date is not None:
            data = D_Date.objects.filter(pk_date=pk_date)
            serializer = DDateSerializer(data, many=True)
            return Response(serializer.data)
        else:
            data = D_Date.objects.all()
            serializer = DDateSerializer(data, many=True)
            return Response(serializer.data)

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
    # http://127.0.0.1:8000/api/cities/63000
    lookup_field = 'postal_code'
    def get(self, request, postal_code=None):
        if postal_code is not None:
            data = City.objects.filter(postal_code=postal_code)
            serializer = CitySerializer(data, many=True)
            return Response(serializer.data)
        else:
            data = City.objects.all()
            serializer = CitySerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, postal_code):
        try:
            city = City.objects.get(postal_code=postal_code)
        except City.DoesNotExist:
            return Response({'error': 'La ville n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, postal_code):
        try:
            city = City.objects.get(postal_code=postal_code)
        except City.DoesNotExist:
            return Response({'error': 'La ville n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CitySerializer(city, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, postal_code):
    #     try:
    #         city = City.objects.get(postal_code=postal_code)
    #     except City.DoesNotExist:
    #         return Response({'error': 'La ville n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     city.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, postal_code):
        queryset = City.objects.filter(postal_code=postal_code).first()
        if postal_code is None:
            return Response({'erreur': f"Veuillez saisir un code postal"}, status=status.HTTP_400_BAD_REQUEST)
        elif queryset is None:
            return Response({'erreur': f"Pas de ville avec ce code postal : {postal_code}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset.delete()
            return Response({'message': f"Ville ({postal_code}) supprimée"}, status=status.HTTP_204_NO_CONTENT)



class Club_api(APIView):
    # http://127.0.0.1:8000/api/clubs/
    def get(self, request, code=None):
        try:
            clubs = F_Club.objects.all()
            paginator = PageNumberPagination()
            paginator.page_size = 3
            result_page = paginator.paginate_queryset(clubs, request)
            serializer = FClubSerializer(result_page, many=True)
            count = clubs.count()


            response_data = {
                'count': count,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link(),
                'results': serializer.data
            }

            return paginator.get_paginated_response(response_data)
        except Exception as e:
            return Response({'erreur': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request):
        serializer = FClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = FClubSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = FClubSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class API_Operational_Data_Store(APIView):
    # api/ods/table/
    """ Voici l\'API de ma base de donnée

        Méthode GET :
        Méthode POST :
        Méthode PUT :
        Méthode PATCH :
        Méthode DELETE :
    """

    def get(self, request, pk=None):

        if 'table_name' in request.GET:
            table_name = request.GET['table_name']
            data = eval(table_name).objects.all()
            count = data.count()
        else:
            data = F_Club.objects.all()
            count = data.count()

        serializer = FClubSerializer(data=data, many=True)
        serializer.is_valid()

        data = serializer.data

        result = {
            'count': count,
            'data': data,
        }

        return Response(data=result, status=status.HTTP_200_OK)


class D_Geographie_api(APIView):
    # api/geographies/74315-CSZ
    """

    """

    def get(self, request, pk_geographie):
        try:
            geographies = D_Geographie.objects.filter(pk_geographie=pk_geographie)
            paginator = PageNumberPagination()
            paginator.page_size = 3
            result_page = paginator.paginate_queryset(geographies, request)
            serializer = D_GeographieSerializer(result_page, many=True)
            response_data = {
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link(),
                'results': serializer.data
            }
            return paginator.get_paginated_response(response_data)
        except Exception as e:
            return Response({'erreur': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk_geographie):
        # api/geographies/74315-CSZ
        try:
            geographie = D_Geographie.objects.get(pk_geographie=pk_geographie)
            print(pk_geographie)
        except D_Geographie.DoesNotExist:
            return Response({'erreur': 'La geographie n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)
        serializer = D_GeographieSerializer(geographie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

