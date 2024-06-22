# Generated by Django 5.0.6 on 2024-06-19 18:44

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0007_rename_idequipment_material_idmaterial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='idEquipment',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='idMaterials',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='idPpe',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='idTool',
        ),
        migrations.AlterField(
            model_name='worker',
            name='contractDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de Contrato'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='dni',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='DNI'),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('idLoan', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('loanDate', models.DateField(default=django.utils.timezone.now)),
                ('returnLoanDate', models.DateField(default=django.utils.timezone.now)),
                ('idEquipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.equipment')),
                ('idMaterials', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.material')),
                ('idPpe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.ppe')),
                ('idTool', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.tool')),
                ('idWorker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.worker')),
            ],
        ),
    ]
