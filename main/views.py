from django.shortcuts import render, get_object_or_404
from .models import Human


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


def human_body_detail(request, slug):
    human = get_object_or_404(Human, slug=slug)
    return render(request, 'main/body-detail.html', {'human': human})


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


def hypophis(request):
    return render(request, 'main/body/hypophis.html', {})


def gland(request):
    return render(request, 'main/body/gland.html', {})


def lungs(request):
    return render(request, 'main/body/lungs.html', {})


def skin(request):
    return render(request, 'main/body/skin.html', {})


def fluid(request):
    return render(request, 'main/body/fluid.html', {})


def stomach(request):
    return render(request, 'main/body/stomach.html', {})


def liver(request):
    return render(request, 'main/body/liver.html', {})


def pancreas(request):
    return render(request, 'main/body/pancreas.html', {})


def sex_gland(request):
    return render(request, 'main/body/sex-gland.html', {})


def muscle(request):
    return render(request, 'main/body/muscle.html', {})


def iron(request):
    return render(request, 'main/body/iron.html', {})


def marganes(request):
    return render(request, 'main/body/marganes.html', {})


def molybdenum(request):
    return render(request, 'main/body/molybdenum.html', {})


def tin(request):
    return render(request, 'main/body/tin.html', {})


def phosphorus(request):
    return render(request, 'main/body/phosphorus.html', {})


def mercury(request):
    return render(request, 'main/body/mercury.html', {})
