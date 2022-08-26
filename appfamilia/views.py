from django.shortcuts import render, HttpResponse
from django.template import loader #Importamos el cargador
from appfamilia.models import Familia
# Create your views here.

def datos_familiares(request):
    persona_1=Familia(nombre = 'Jose Soto',parentesco = 'padre', edad = 60, fecha_nacimiento = '1962-6-2')
    persona_1.save()

    persona_2 = Familia(nombre='Marisol Reyes', parentesco='Madre',edad=60, fecha_nacimiento='1962-08-09')
    persona_2.save()

    persona_3 = Familia(nombre='Yoselin', parentesco='Esposa', edad=26, fecha_nacimiento='1996-03-28')
    persona_3.save()

    persona_4 = Familia(nombre='Vanessa Soto', parentesco='Hermana',edad=37, fecha_nacimiento='1985-02-02')
    persona_4.save()

    persona_5 = Familia(nombre='Esperanza Soto', parentesco='Hermana', edad=27, fecha_nacimiento='1995-10-12')
    persona_5.save()

    plantilla= loader.get_template('datos_familia.html')

    familiares = {'familiar':[persona_1, persona_2, persona_3, persona_4,persona_5]}

    documento=plantilla.render(familiares)

    return HttpResponse(documento)