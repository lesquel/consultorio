from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Perfil

# Definir una clase inline para el perfil
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False

# Extender el UserAdmin para incluir el Perfil
class UserAdmin(BaseUserAdmin):
    inlines = [PerfilInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        try:
            # Intenta acceder al perfil
            obj.perfil
        except Perfil.DoesNotExist:
            # Si el perfil no existe, no lo creamos aquí
            return super().get_inline_instances(request, obj)
        return super(UserAdmin, self).get_inline_instances(request, obj)

# Desregistrar el UserAdmin por defecto y registrar el nuevo UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
