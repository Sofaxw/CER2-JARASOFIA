# Generated by Django 4.2.6 on 2023-10-22 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miapp', '0002_alter_entidad_options_alter_comunicado_detalle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntidadAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='modificado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunicado_modificado', to='miapp.entidadadmin'),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='publicado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunicado_publicado', to='miapp.entidadadmin'),
        ),
    ]
