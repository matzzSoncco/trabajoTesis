from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from .Equipment import Equipment
from .Tool import Tool
from .Material import Material
from .Ppe import Ppe
from .Worker import Worker
from django.utils import timezone

class Loan(models.Model):
    idLoan = models.UUIDField(verbose_name=_('ID'), primary_key=True, default=uuid.uuid4, editable=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    ppe = models.ForeignKey(Ppe, on_delete=models.CASCADE, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    loanDate = models.DateField(verbose_name=_('Fecha de Entrega'), default=timezone.now)
    returnLoanDate = models.DateField(verbose_name=_('Fecha de Devolución'), default=timezone.now)