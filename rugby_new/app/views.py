from django.shortcuts import render
from app.models import Player, ODS
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    data_ods = ODS.objects.all()
    nombre_lignes_ods = ODS.objects.count()
    context = {'data_ods': data_ods, 'nombre_lignes_ods': nombre_lignes_ods}
    return render(request, 'index.html', context=context)


def ods_data(request):
    data_ods = ODS.objects.all()
    paginator = Paginator(data_ods, 5)

    page = request.GET.get('page')

    try:
        data_ods = paginator.page(page)
    except PageNotAnInteger:
        data_ods = paginator.page(1)
    except EmptyPage:

        data_ods = paginator.page(paginator.num_pages)


    context = {'data_ods': data_ods}

    return render(request, 'display_data.html', context=context)


def contact(request):
    context = {'contact': 'coach'}
    return render(request, 'contact.html', context=context)
