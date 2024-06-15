from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Material(models.Model):
    idEquipment = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(verbose_name=_('Nombre'), null=False, max_length=20)
    quantity = models.IntegerField(verbose_name=_('Cantidad'), validators=[MinValueValidator(0)], null=False, default=0)
    stock = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "%s %s %s %s" %(self.idEquipment, self.name, self.quantity, self.stock)