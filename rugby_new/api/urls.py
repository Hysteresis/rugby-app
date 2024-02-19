from django.urls import path

from api.views import EndPointClub, City_api, Date_api

urlpatterns = [
    path('', EndPointClub.as_view()),
    path('dates/', Date_api.as_view(), name='dates'),
    path('update-date/', Date_api.as_view(), name='update-date'),
    path('cities/', City_api.as_view(), name='cities'),
    path('cities/<str:name>/', City_api.as_view(), name='city-detail')
]


