"""
URL configuration for biblioteka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from folder_aplikacji import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kategorie/', views.kategoria_list),
    path('kategorie/<int:pk>/', views.kategoria_details),
    path('autorzy/', views.autor_list),
    path('autorzy/<int:pk>/', views.autor_details),
    path('ksiazki/', views.ksiazka_list),
    path('ksiazki/<int:pk>/', views.ksiazka_details),
    path('czytelnicy/', views.czytelnik_list),
    path('czytelnicy/<int:pk>/', views.czytelnik_details),
    path('wypozyczenia/', views.wypozyczenie_list),
    path('wypozyczenia/<int:pk>/', views.wypozyczenie_details),
    path('ksiazki_html/', views.ksiazki_list_html),
    path('ksiazki_html/<int:id>/', views.ksiazki_detail_html),
    path('welcome/', views.welcome_view),
]