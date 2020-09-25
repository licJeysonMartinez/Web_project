from django.db import models

# Create your models here.
class Reservar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    fecha = models.DateField()
    hora = models.TimeField()
    numero_comensales = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
