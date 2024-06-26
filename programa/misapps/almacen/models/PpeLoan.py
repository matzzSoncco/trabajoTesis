from django.db import models
from .Ppe import Ppe
from .Worker import Worker
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class PpeLoan(models.Model):
    idPpeLoan = models.AutoField(primary_key=True, editable=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    ppe = models.ForeignKey(Ppe, on_delete=models.CASCADE, null=True)
    durations = models.IntegerField(verbose_name=_('Duración'), null=False, default=0)
    loanDate = models.DateField(verbose_name=_('Fecha de Entrega'), default=timezone.now)
    newLoanDate = models.DateField(verbose_name=_('Fecha de Nueva Entrega'), default=timezone.now)