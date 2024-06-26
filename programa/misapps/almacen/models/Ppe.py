from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class Ppe(models.Model):
    idPpe = models.CharField(verbose_name=_('ID'), primary_key=True, editable=False, max_length=10)
    name = models.CharField(verbose_name=_('Nombre'), null=False, max_length=20)
    quantity = models.IntegerField(verbose_name=_('Cantidad'), validators=[MinValueValidator(0)], null=False, default=0)
    unitCost = models.DecimalField(verbose_name=_('Costo Unitario'), default=0.0, null=False, max_digits=8, decimal_places=2)
    totalCost = models.DecimalField(verbose_name=_('Costo Total'), default=0.0, null=False, max_digits=10, decimal_places=2, editable=False)
    guideNumber = models.IntegerField(verbose_name=_('Número de Guía'), null=False, default=0)
    stock = models.IntegerField(null=False, default=0)
    unit = models.CharField(verbose_name=_('Unidad'), null=False, max_length=20, default='')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcula el totalCosto antes de guardar
        self.totalCost = self.unitCost * self.quantity
        
        if not self.idPpe or not self.idPpe.startswith('EPP-'):
            # Obtiene el número autoincrementable
            last_id = Ppe.objects.all().order_by('-idPpe').first()
            if last_id:
                # Intenta obtener el número del último idPpe
                try:
                    last_id_number = int(last_id.idPpe.split('-')[1]) + 1
                except IndexError:
                    # Si hay un IndexError, asigna 1 como el siguiente número
                    last_id_number = 1
            else:
                last_id_number = 1
            
            # Forma el nuevo ID con el formato EPP-numero
            self.idPpe = f'EPP-{last_id_number:04}'  # '04' asegura que siempre tenga 4 dígitos
        
        super(Ppe, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.idPpe} {self.name} {self.quantity} {self.unitCost} {self.totalCost} {self.stock}"