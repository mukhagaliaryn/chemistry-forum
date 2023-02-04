from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {})


def about(request):
    return render(request, 'main/about.html', {})


def table(request):
    return render(request, 'main/table.html', {})


def contact(request):
    return render(request, 'main/contact.html', {})
