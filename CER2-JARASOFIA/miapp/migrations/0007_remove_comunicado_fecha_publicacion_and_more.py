# Generated by Django 4.2.6 on 2023-10-24 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miapp', '0006_alter_comunicado_modificado_por_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunicado',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='comunicado',
            name='fecha_ultima_modificación',
        ),
        migrations.AddField(
            model_name='entidad',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
    ]