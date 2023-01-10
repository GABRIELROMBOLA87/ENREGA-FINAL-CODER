from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class Post(models.Model):
    Repuesto = models.CharField(max_length=100)
    Vehiculo = models.CharField(max_length=100)
    Detalle = models.TextField(max_length=3000)
    Precio = models.IntegerField()
    imagen = models.ImageField(upload_to="posteos", null="True", blank=True)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", null="True", blank=True)
    
class Mensaje(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    enviado_el = models.DateField(auto_now_add=True)


