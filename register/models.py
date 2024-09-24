# archivo models.py
from django.db import models

from django.contrib.auth.models import User

# Perfil es una clase que representa el perfil de un usuario
class Perfil(models.Model):
    # ROLE_CHOICES es una tupla de tuplas que contiene los roles disponibles para el usuario
    ROLE_CHOICES = (
        ('usuario', 'Usuario'),
        ('doctor', 'Doctor'),
        ('asistente', 'Asistente'),
    )
    # user es una referencia a la clase User de django.contrib.auth.models
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # rol es un campo de tipo CharField que almacena el rol del usuario
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default='usuario')

    def __str__(self):
        return f"{self.user.username} - {self.get_rol_display()}"
    