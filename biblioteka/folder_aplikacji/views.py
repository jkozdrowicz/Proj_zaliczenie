from datetime import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import Autor, Czytelnik, Kategoria, Ksiazka, Wypozyczenie
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login

from .serializers import AutorSerializer, CzytelnikSerializer, KategoriaSerializer, KsiazkaSerializer, WypozyczenieSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])    
def kategoria_details(request, pk):
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        kategoria = Kategoria.objects.get(pk=pk)
        serializer = KategoriaSerializer(kategoria)
        return Response(serializer.data)

@api_view(['GET'])
def kategoria_list_get(request):
    kategorie = Kategoria.objects.all()
    serializer = KategoriaSerializer(kategorie, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def kategoria_list_post(request):
    serializer = KategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def kategoria_update(request, pk):
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = KategoriaSerializer(kategoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])    
def kategoria_delete(request, pk): 
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        kategoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])    
def autor_details(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

@api_view(['GET'])
def autor_list_get(request):
    autorzy = Autor.objects.all()
    serializer = AutorSerializer(autorzy, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def autor_list_post(request):
    serializer = AutorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def autor_update(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])    
def autor_delete(request, pk): 
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET'])
def czytelnik_list_get(request):
    czytelnicy = Czytelnik.objects.all()
    serializer = CzytelnikSerializer(czytelnicy, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def czytelnik_list_post(request):
    serializer = CzytelnikSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def czytelnik_details(request, pk):
    try:
        czytelnik = Czytelnik.objects.get(pk=pk)
    except Czytelnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CzytelnikSerializer(czytelnik)
    return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def czytelnik_update(request, pk):
    try:
        czytelnik = Czytelnik.objects.get(pk=pk)
    except Czytelnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CzytelnikSerializer(czytelnik, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def czytelnik_delete(request, pk):
    try:
        czytelnik = Czytelnik.objects.get(pk=pk)
    except Czytelnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    czytelnik.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# KSIAZKI
@api_view(['GET'])
def ksiazka_list_get(request):
    ksiazki = Ksiazka.objects.all()
    serializer = KsiazkaSerializer(ksiazki, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ksiazka_list_post(request):
    serializer = KsiazkaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ksiazka_details(request, pk):
    try:
        ksiazka = Ksiazka.objects.get(pk=pk)
    except Ksiazka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = KsiazkaSerializer(ksiazka)
    return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def ksiazka_update(request, pk):
    try:
        ksiazka = Ksiazka.objects.get(pk=pk)
    except Ksiazka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = KsiazkaSerializer(ksiazka, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ksiazka_delete(request, pk):
    try:
        ksiazka = Ksiazka.objects.get(pk=pk)
    except Ksiazka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ksiazka.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# WYPOŻYCZENIA
@api_view(['GET'])
def wypozyczenie_list_get(request):
    wypozyczenia = Wypozyczenie.objects.all()
    serializer = WypozyczenieSerializer(wypozyczenia, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def wypozyczenie_list_post(request):
    serializer = WypozyczenieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def wypozyczenie_details(request, pk):
    try:
        wypozyczenie = Wypozyczenie.objects.get(pk=pk)
    except Wypozyczenie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = WypozyczenieSerializer(wypozyczenie)
    return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def wypozyczenie_update(request, pk):
    try:
        wypozyczenie = Wypozyczenie.objects.get(pk=pk)
    except Wypozyczenie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = WypozyczenieSerializer(wypozyczenie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wypozyczenie_delete(request, pk):
    try:
        wypozyczenie = Wypozyczenie.objects.get(pk=pk)
    except Wypozyczenie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    wypozyczenie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

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
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Error creating your account')
    else:
        form = UserCreationForm()
    return render(request, 'folder_aplikacji\\rejestracja\\rejestracja.html', {'form': form})

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return redirect('home')