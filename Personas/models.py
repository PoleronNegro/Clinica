from django.db import models
#importacion realizada por oscar
from Detalle import models as detalleModelo
# Create your models here.

#clase creada por matías (persona)
class Persona(models.Model):
    #realice una actualizacion de datos Oscar Torres
    run = models.CharField(max_length=10, null=false, blank=false)
    nombre = models.CharField(max_length=30, null=false, blank=false)
    apellido = models.CharField(max_length=30, null=false, blank=false)
    #columna genero añadida por oscar
    idgenero = models.ForeignKey(detalleModelo.Genero.idgenero,on_delete = models.CASCADE)
    telefono = models.IntegerField(null=false, blank=false)
    correo = models.EmailField(max_length=45, null=false, blank=false)
    direccion = models.CharField(max_length=30, null=false, blank=false)
    #columna comuna añadida por oscar
    idcomuna = models.ForeignKey(detalleModelo.Comuna.idcomuna,on_delete = models.CASCADE)

#clase creada por matías (medico)
class Medico(models.Model):
    run = models.ForeignKey(Persona.run, null=false, blank=false)
    id_especialidad = models.ForeignKey(Especialidad.id_especialidad, null=false, blank=false)
    id_horario = models.ForeignKey(Horario.id_horario, null=false, blank=false)

#clase creada por matías (paciente)
class Paciente(models.Model):
    run = models.ForeignKey(Persona.run, null=false, blank=false)
    estado = models.BooleanField(default=true)