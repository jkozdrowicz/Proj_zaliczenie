from datetime import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Autor, Czytelnik, Kategoria, Ksiazka, Wypozyczenie
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import AutorSerializer, CzytelnikSerializer, KategoriaSerializer, KsiazkaSerializer, WypozyczenieSerializer

@api_view(['GET', 'POST'])
def kategoria_list(request):
    if request.method == 'GET':
        osoby = Kategoria.objects.all()
        serializer = KategoriaSerializer(osoby, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = KategoriaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])    
def kategoria_details(request, pk):
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = KategoriaSerializer(kategoria)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        kategoria.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def autor_list(request):
    if request.method == 'GET':
        osoby = Autor.objects.all()
        serializer = AutorSerializer(osoby, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])    
def autor_details(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AutorSerializer(autor)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        Autor.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def ksiazka_list(request):
    if request.method == 'GET':
        osoby = Ksiazka.objects.all()
        serializer = KsiazkaSerializer(osoby, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = KsiazkaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])    
def ksiazka_details(request, pk):
    try:
        ksiazka = Ksiazka.objects.get(pk=pk)
    except Ksiazka.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = KsiazkaSerializer(ksiazka)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        ksiazka.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def czytelnik_list(request):
    if request.method == 'GET':
        osoby = Czytelnik.objects.all()
        serializer = CzytelnikSerializer(osoby, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CzytelnikSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])    
def czytelnik_details(request, pk):
    try:
        czytelnik = Czytelnik.objects.get(pk=pk)
    except Czytelnik.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CzytelnikSerializer(czytelnik)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        czytelnik.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def wypozyczenie_list(request):
    if request.method == 'GET':
        osoby = Wypozyczenie.objects.all()
        serializer = WypozyczenieSerializer(osoby, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = WypozyczenieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])    
def wypozyczenie_details(request, pk):
    try:
        wypozyczenie = Wypozyczenie.objects.get(pk=pk)
    except Wypozyczenie.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = WypozyczenieSerializer(wypozyczenie)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        wypozyczenie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
def welcome_view(request):
    now = datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def ksiazki_list_html(request):
    # pobieramy wszystkie obiekty ksiazki z bazy poprzez QuerySet
    ksiazkis = Ksiazka.objects.all()
    return render(request,
                  "folder_aplikacji/ksiazki/list.html",
                  {'ksiazkas': ksiazkis})

def ksiazki_detail_html(request, id):
    # pobieramy konkretny obiekt ksiazki
    try:
        ksiazki = Ksiazka.objects.get(id=id)
    except Ksiazka.DoesNotExist:
        raise Http404("Obiekt ksiazki o podanym id nie istnieje")

    return render(request,
                  "folder_aplikacji/ksiazki/detail.html",
                  {'ksiazka': ksiazki})