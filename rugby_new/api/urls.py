from django.urls import path

from api.views import EndPointClub, City_api, Date_api

urlpatterns = [
    path('', EndPointClub.as_view()),
    path('dates/', Date_api.as_view(), name='dates'),
    path('dates/<str:pk_date>/', Date_api.as_view(), name='date-detail'),
    path('update-date/', Date_api.as_view(), name='update-date'),
    path('cities/', City_api.as_view(), name='cities'),
    path('cities/<str:postal_code>/', City_api.as_view(), name='city-postal-code')
]


