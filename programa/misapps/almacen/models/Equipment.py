from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Equipment(models.Model):
    idEquipment = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(verbose_name=_('Nombre'), null=False, max_length=20)
    quantity = models.IntegerField(verbose_name=_('Cantidad'), null=False, default=0)
    LEVELS = [
        (0, 'Elija un nivel'),
        (1, 'Bajo'),
        (2, 'Medio'),
        (3, 'Mayor')
    ]
    level = models.IntegerField(verbose_name=_('Nivel'), null=False, choices=LEVELS, default=0)
    stock = models.IntegerField(verbose_name=_('Stock'), null=False, default=0)

    def __str__(self):
        return "%s %s %s %s %s" %(self.idEquipment, self.name, self.quantity, self.level, self.stock)