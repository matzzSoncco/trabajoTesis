# Generated by Django 5.0.6 on 2024-06-14 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_alter_ppe_name_alter_ppe_totalcost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ppe',
            old_name='cantity',
            new_name='quantity',
        ),
    ]