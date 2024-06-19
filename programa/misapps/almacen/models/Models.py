# misapps/almacen/models.py

from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    stock = models.IntegerField()
    archivo = models.FileField(upload_to='archivos/', blank=True, null=True)  # Aquí se define el campo archivo

