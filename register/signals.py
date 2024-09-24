from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def crear_o_guardar_perfil_usuario(sender, instance, created, **kwargs):
    # Usa get_or_create para evitar duplicados
    Perfil.objects.get_or_create(user=instance)