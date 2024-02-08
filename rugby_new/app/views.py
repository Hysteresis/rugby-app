from django.shortcuts import render
from app.models import Player, ODS


# Create your views here.
def index(request):
    players = Player.objects.all()
    # Player.objects.get_or_create()
    context = {'players': players}

    return render(request, 'index.html', context=context)


def ods_data(request):
    data_ods = ODS.objects.all()
    context = {'data_ods': data_ods}

    return render(request, 'display_data.html', context=context)


def contact(request):
    context = {'contact': 'coach'}
    return render(request, 'contact.html', context=context)
