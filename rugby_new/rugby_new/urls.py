"""
URL configuration for rugby_new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import index, ods_data, run_etl_ods
from app.views import contact
from api import urls as api_urls


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('ods/', ods_data, name='ods_data'),
    path('api/', include(api_urls)),
    path('api/update-date/', include(api_urls), name='api_update_date'),
    path('etl_ods', run_etl_ods, name='run_etl_ods'),
    path('contact/', contact),
]
