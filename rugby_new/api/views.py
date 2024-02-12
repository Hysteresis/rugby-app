from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from app.models import ODS


# Create your views here.
class EndPointDWH(APIView):
    """Here my first API
    get arg:
    - table
    """
    def get(self, request):
        # table = request.GET['table'] je recupère une table de fait
        # result = {'message': 'All is ok', 'table': table, 'result': 320}
        result = {
            'message': 'All is ok'
        }

        return Response(result)



# class (APIView):
#     def get(self, request):
#         return
