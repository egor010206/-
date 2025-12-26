from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница'
    }
    return render(request, 'main/index.html', context)

def registr(request):
    return render(request, 'main/registr.html')

def vhod(request):
    return render(request, 'main/vhod.html')