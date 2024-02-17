from django.urls import path

from api.views import EndPointClub

urlpatterns = [
    path('', EndPointClub.as_view()),
]