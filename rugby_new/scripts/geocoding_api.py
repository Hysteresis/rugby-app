import requests

from app.models import D_Geographie


class Geocoding:

    def get_departement(self, value):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'key': 'my api _key', #Google API KEY
            'address': value
        }

        result = requests.get(url, params=params)
        data = result.json()
        print(data)

        if 'results' in data and data['results']:
            address_components = data['results'][0]['address_components']
            if len(address_components) >= 2:
                return address_components[1]['long_name']

        return "Département non trouvé"

def run():
    geo = Geocoding()
    geocoding = D_Geographie.objects.values_list('pk_geographie', 'code_commune', 'commune').distinct()[:10]
    for pk_geographie, code_commune, commune in geocoding:
        value = f"{code_commune} - {commune}"
        department = geo.get_departement(value)
        print(f"Code commune: {code_commune}, Commune: {commune}, Department: {department}")

        instance = D_Geographie.objects.get(pk=pk_geographie)
        instance.nom_departement = department
        # instance.save()
