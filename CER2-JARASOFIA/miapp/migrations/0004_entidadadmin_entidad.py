# Generated by Django 4.2.6 on 2023-10-22 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_entidadadmin_alter_comunicado_modificado_por_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidadadmin',
            name='entidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miapp.entidad'),
        ),
    ]
