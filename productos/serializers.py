from rest_framework import serializers
from .models import Chela, ChelaFavorita


class ChelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chela  
        fields = '__all__'


class ChelaFavoritaSerializer(serializers.ModelSerializer):
    chela = ChelaSerializer()

    class Meta:
        model = ChelaFavorita
        fields = '__all__'
