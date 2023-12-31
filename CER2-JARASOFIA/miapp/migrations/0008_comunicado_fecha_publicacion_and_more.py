# Generated by Django 4.2.6 on 2023-10-24 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0007_remove_comunicado_fecha_publicacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comunicado',
            name='fecha_ultima_modificación',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
