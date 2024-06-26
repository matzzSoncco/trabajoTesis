from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Equipment(models.Model):
    idEquipment = models.CharField(verbose_name=_('ID'), primary_key=True, editable=False, max_length=10)
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
    guideNumber = models.IntegerField(verbose_name=_('Número de Guía'), null=False, default=0)
    #status = models.BooleanField(verbose_name=_('Estado'), default=False)

    def save(self, *args, **kwargs):
        if not self.idEquipment or not self.idEquipment.startswith('E-'):
            # Obtiene el número autoincrementable
            last_id = Equipment.objects.all().order_by('-idEquipment').first()
            if last_id:
                # Intenta obtener el número del último idEquipment
                try:
                    last_id_number = int(last_id.idEquipment.split('-')[1]) + 1
                except IndexError:
                    # Si hay un IndexError, asigna 1 como el siguiente número
                    last_id_number = 1
            else:
                last_id_number = 1
            
            self.idEquipment = f'M-{last_id_number:04}'  # '04' asegura que siempre tenga 4 dígitos
        
        super(Equipment, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s" %(self.idEquipment, self.name, self.quantity, self.level, self.stock)