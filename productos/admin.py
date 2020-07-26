from django.contrib import admin
# Register your models here.

from .models import Chela, ChelaFavorita

admin.site.register(Chela)
admin.site.register(ChelaFavorita)