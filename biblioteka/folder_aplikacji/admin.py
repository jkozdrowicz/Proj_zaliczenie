from django.contrib import admin
from .models import Kategoria, Autor, Ksiazka, Czytelnik, Wypozyczenie

admin.site.register(Kategoria)
admin.site.register(Autor)
admin.site.register(Ksiazka)
admin.site.register(Czytelnik)
admin.site.register(Wypozyczenie)