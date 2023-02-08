from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('table/', views.table, name='table'),
    path('contact/', views.contact, name='contact'),
    path('human-body/', views.human_body, name='human_body'),
    path('human-body/<slug>/', views.human_body_detail, name='human_body_detail'),

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
    path('body/hypophis/', views.hypophis, name='hypophis'),
    path('body/gland/', views.gland, name='gland'),
    path('body/lungs/', views.lungs, name='lungs'),
    path('body/skin/', views.skin, name='skin'),
    path('body/fluid/', views.fluid, name='fluid'),
    path('body/stomach/', views.stomach, name='stomach'),
    path('body/liver/', views.liver, name='liver'),
    path('body/pancreas/', views.pancreas, name='pancreas'),
    path('body/sex-gland/', views.sex_gland, name='sex_gland'),
    path('body/muscle/', views.muscle, name='muscle'),

    path('body/iron/', views.iron, name='iron'),
    path('body/marganes/', views.marganes, name='marganes'),
    path('body/molybdenum/', views.molybdenum, name='molybdenum'),
    path('body/tin/', views.tin, name='tin'),
    path('body/phosphorus/', views.phosphorus, name='phosphorus'),
    path('body/mercury/', views.mercury, name='mercury'),
]
