from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from app.models import F_Club, D_Federation, D_Geographie
from app import serializers
from app.serializers import FClubSerializer, DFederationSerializer
from rest_framework.pagination import PageNumberPagination


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
