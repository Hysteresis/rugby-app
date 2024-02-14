from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from app.models import ODS


# Create your views here.
class EndPointDWH(APIView):
    """Here my first API
    get arg:
    - table
    """
    def get(self, request):
        result = {
            'message': 'All is ok'
        }

        return Response(result)

    def post(self, request):
        data = request.data
        result = {
            'message': 'POST a fonctionné',
            'data': data
        }
        return Response(result, status=status.HTTP_201_CREATED)
