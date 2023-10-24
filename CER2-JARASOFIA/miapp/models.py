from django.db import models
from django.contrib.auth.models import User

TIPO_CHOICES= [
    ("S", "Suspensión de actividades"),
    ("C", "Suspensión de clase"),
    ("I", "Información"),]





class Entidad(models.Model):
    id= models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=80)
    logo= models.ImageField(null=True, blank=True)
    admin= models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    

    def __str__(self) -> str:
        return self.nombre
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"


class Comunicado(models.Model):
    id= models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=100)
    detalle= models.CharField(max_length=200)
    detalle_corto= models.CharField(max_length=60)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    entidad= models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible= models.BooleanField(default=False) 
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificación= models.DateTimeField(auto_now=True)
    publicado_por= models.ForeignKey(User, related_name='comunicado_publicado', on_delete=models.CASCADE)
    modificado_por= models.ForeignKey(User, related_name='comunicado_modificado',on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

