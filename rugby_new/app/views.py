from django.shortcuts import render



# Create your views here.
def index(request):
    context = {'ball': 'grand'}
    return render(request, 'index.html', context=context)

def contact(request):
    context = {'contact': 'coach'}
    return render(request, 'contact.html', context=context)
