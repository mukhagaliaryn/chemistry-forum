from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {})


def about(request):
    return render(request, 'main/about.html', {})


def table(request):
    return render(request, 'main/table.html', {})


def contact(request):
    return render(request, 'main/contact.html', {})


# Human body
# ----------------------------------------------------------------------
def human_body(request):
    return render(request, 'main/body.html', {})


def hair(request):
    return render(request, 'main/body/hair.html', {})


def brain(request):
    return render(request, 'main/body/brain.html', {})


def retina(request):
    return render(request, 'main/body/retina.html', {})


def eye(request):
    return render(request, 'main/body/eye.html', {})


def tooth(request):
    return render(request, 'main/body/tooth.html', {})


def heart(request):
    return render(request, 'main/body/heart.html', {})


def blood(request):
    return render(request, 'main/body/blood.html', {})


def kidney(request):
    return render(request, 'main/body/kidney.html', {})


def bones(request):
    return render(request, 'main/body/bones.html', {})


def nails(request):
    return render(request, 'main/body/nails.html', {})
