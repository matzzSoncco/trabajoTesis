from django.db import models
from django.utils.translation import gettext_lazy as _

class Worker(models.Model):
    idWorker = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(verbose_name=_('Nombres'), null=False, max_length=20)
    surname = models.CharField(verbose_name=_('Apellido'), null=False, max_length=20)
#_________________________________________________________________________________________________________
    archivo = models.FileField(verbose_name=_('Archivo'), upload_to='archivos/', blank=True, null=True)

    def __str__(self):
        return "%s %s %s" %(self.idWorker, self.name, self.surname)