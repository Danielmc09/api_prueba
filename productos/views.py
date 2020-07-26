# Django
from rest_framework import viewsets

# app
from .models import Chela, ChelaFavorita
from .serializers import ChelaSerializer, ChelaFavoritaSerializer


class ChelaViewSet(viewsets.ModelViewSet):
    queryset = Chela.objects.all()
    serializer_class = ChelaSerializer


class ChelaFavoritaViewSet(viewsets.ModelViewSet):
    queryset = ChelaFavorita.objects.all()
    serializer_class = ChelaFavoritaSerializer

    