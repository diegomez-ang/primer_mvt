from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.template import loader, Template
from django.http import HttpResponse
from Desafio_MVT.models import Familiares


# Función familiares

def familiares(request, name, num_id, date_birth):
    '''
    fam = Familiares(name = 'Flor Marina', num_id= 14562365, date_birth = '15/11/1954')
    fam.save()

    return HttpResponse('Familiar guardado')
    '''
    fam = Familiares(name = name, num_id = num_id, date_birth = date_birth)
    fam.save()
    plantilla = loader.get_template('familiares.html')
    contexto = {
        'name': fam.name,
        'num_id': fam.num_id,
        'date_birth': fam.date_birth
    }
    documento = plantilla.render(contexto)

    return HttpResponse(documento)
