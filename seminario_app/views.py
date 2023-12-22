from django.shortcuts import redirect, render

from . models import Inscritos, Institucion
from . import forms
from django.http import JsonResponse
from . serializers import InscritosSerializers, InstitucionSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'index.html')


def inscribir(request):
    form = forms.FormRegistro()
    if (request.method == 'POST'):
        form = forms.FormRegistro(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)   
    
    data = {'form' : form}
    return render(request, 'inscribirParticipantes.html', data)


def agregarInstitucion(request):
    form = forms.FormInstitucion()
    if (request.method == 'POST'):
        form = forms.FormInstitucion(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    
    data = {'form' : form}
    return render(request, 'agregarInstitucion.html', data)




#.................................. API REST AUTOR.......................................

def autor(request):
    autor = {
        'rut': '18.198.893-2',
        'nombre': 'Ruth Morales',
        'Fecha': '22-12-2023',
        'Asignatura': 'Programacion Back-end',
        'Carrera': 'Analista Programador'
    }
    return JsonResponse(autor)


#.......................CLASS BASED VIEWS MODELO INSCRITOS...............................
class InscritosList_class(APIView):
    def get(self, request):
        insc = Inscritos.objects.all()
        serial = InscritosSerializers(insc, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = InscritosSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)

class InscritosDetalle_class(APIView):
    def get_object(self, id):
        try:
            return Inscritos.objects.get(pk=id)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get (self, request, id):
        insc = self.get_object(id)
        serial = InscritosSerializers(insc)
        return Response(serial.data)
    
    def put (self, request, id):
        insc = self.get_object(id)
        serial = InscritosSerializers(insc, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, id):
        insc = self.get_object(id)
        insc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
#.........................FUNCIÓN BASED VIEWS MODELO INSTITUCION..........................
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        inst = Institucion.objects.all()
        serial = InstitucionSerializers(inst, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        inst = Institucion.objects.get(pk=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializers(inst)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InstitucionSerializers(inst, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        inst.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    














