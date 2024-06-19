from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Equipment(models.Model):
    idEquipment = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(verbose_name=_('Nombre'), max_length=20)
    quantity = models.IntegerField(verbose_name=_('Cantidad'), default=0)
    LEVELS = [
        (0, 'Elija un nivel'),
        (1, 'Bajo'),
        (2, 'Medio'),
        (3, 'Mayor')
    ]
    level = models.IntegerField(verbose_name=_('Nivel'), choices=LEVELS, default=0)
    stock = models.IntegerField(verbose_name=_('Stock'), default=0)
    
    #------------------------------------Se añadio la opcion de ----------------------------------------
    archivo = models.FileField(verbose_name=_('Archivo'), upload_to='archivos/', null=True, blank=True)

    def __str__(self):
        return f'{self.idEquipment} - {self.name} - Nivel: {self.get_level_display()}'
