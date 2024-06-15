from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class Ppe(models.Model):
    idPpe = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(verbose_name=_('Nombre'), null=False, max_length=20)
    quantity = models.IntegerField(verbose_name=_('Cantidad'), validators=[MinValueValidator(0)], null=False, default=0)
    unitCost = models.DecimalField(verbose_name=_('Costo Unitario'), default=0.0, null=False, max_digits=8, decimal_places=2)
    totalCost = models.DecimalField(verbose_name=_('Costo Unitario'), default=0.0, null=False, max_digits=10, decimal_places=2, editable=False)
    stock = models.IntegerField(null=False, default=0)

    def save(self, *args, **kwargs):
        self.totalCost = self.unitCost * self.quantity
        super(Ppe, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s %s" %(self.idPpe, self.name, self.quantity, self.unitCost, self.totalCost, self.stock)