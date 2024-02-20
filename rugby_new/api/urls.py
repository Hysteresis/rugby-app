from django.urls import path

from api.views import EndPointClub, City_api, Date_api, Club_api, API_Operational_Data_Store, D_Geographie_api
app_name = 'api'
urlpatterns = [
    path('', EndPointClub.as_view(), name='endpoint'),
    path('ods/table/', API_Operational_Data_Store.as_view()),
    path('dates/', Date_api.as_view(), name='dates'),
    path('dates/<str:pk_date>/', Date_api.as_view(), name='date-detail'),
    path('update-date/', Date_api.as_view(), name='update-date'),
    path('cities/', City_api.as_view(), name='cities'),
    path('cities/<str:postal_code>/', City_api.as_view(), name='city-postal-code'),
    path('clubs/', Club_api.as_view(), name='clubs'),
    path('geographies/', D_Geographie_api.as_view(), name='geographies'),
    path('geographies/<str:pk_geographie>', D_Geographie_api.as_view(), name='geographies'),

]


