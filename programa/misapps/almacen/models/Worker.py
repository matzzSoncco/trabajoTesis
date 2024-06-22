from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Worker(models.Model):
    dni = models.IntegerField(verbose_name=_('DNI'), primary_key=True, default=0)
    position = models.CharField(verbose_name=_('Cargo'), null=False, max_length=20, default=None)
    contractDate = models.DateField(verbose_name=_('Fecha de Contrato'), default=timezone.now)
    name = models.CharField(verbose_name=_('Nombres'), null=False, max_length=20)
    surname = models.CharField(verbose_name=_('Apellidos'), null=False, max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s %s" %(self.dni, self.name, self.surname)