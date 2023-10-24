from django.contrib import admin
from .models import Entidad
from .models import Comunicado



class AdminComunicado(admin.ModelAdmin):
    
    readonly_fields= ('publicado_por', 'modificado_por', 'entidad')

    def save_model(self, request, obj, form, change):
        usuario =request.user
        entidad= Entidad.objects.filter(admin=usuario).first()
        obj.entidad= entidad
        obj.publicado_por = usuario
        obj.modificado_por = usuario
        super(AdminComunicado, self).save_model(request, obj, form, change)


    def get_queryset(self, request):
        usuario= request.user
        queryset= super(AdminComunicado, self).get_queryset(request)
        queryset= queryset.filter(publicado_por = request.user)
        queryset= queryset.filter(modificado_por = request.user)
        return queryset


admin.site.register(Entidad)
admin.site.register(Comunicado, AdminComunicado)


