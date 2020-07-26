from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Chela(models.Model):
    marca = models.CharField(max_length=50)
    alcohol = models.DecimalField(max_digits=4, decimal_places=2)
    mililitros = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.marca


class ChelaFavorita(models.Model):
    chela = models.ForeignKey(Chela, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


