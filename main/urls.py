from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('table/', views.table, name='table'),
    path('contact/', views.contact, name='contact'),
    path('human-body/', views.human_body, name='human_body'),

    path('body/hair/', views.hair, name='hair'),
    path('body/brain/', views.brain, name='brain'),
    path('body/retina/', views.retina, name='retina'),
    path('body/eye/', views.eye, name='eye'),
    path('body/tooth/', views.tooth, name='tooth'),
    path('body/heart/', views.heart, name='heart'),
    path('body/blood/', views.blood, name='blood'),
    path('body/kidney/', views.kidney, name='kidney'),
    path('body/bones/', views.bones, name='bones'),
    path('body/nails/', views.nails, name='nails'),
]
