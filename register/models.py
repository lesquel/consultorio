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
    
class Sexo(models.Model):
    sexo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sexo}"

class InfoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.SmallIntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    telefono = models.SmallIntegerField(max_length=50)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, null=True, blank=True)
    fecha_nacimiento = models.DateField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.nombre} {self.apellido}"