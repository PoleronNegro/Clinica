from django.db import models
#importacion realizada por oscar
from Detalle import models as detalleModelo
# Create your models here.

#clase creada por matías (persona)
class Persona(models.Model):
    run = models.CharField(primarykey=true, max_length=10, null=false, blank=false)
    nombre = models.CharField(max_length=30, null=false, blank=false)
    apellido = models.CharField(max_length=30, null=false, blank=false)
    id_genero = models.ForeignKey(Genero.id_genero, null=false, blank=false)    
    telefono = models.CharField(max_length=12, null=false, blank=false)
    correo = models.CharField(max_length=45, null=false, blank=false)
    direccion = models.CharField(max_length=30, null=false, blank=false)
    id_ciudad = models.ForeignKey(Ciudad.id_ciudad, null=false, blank=false)

#clase creada por matías (medico)
class Medico(models.Model):
    run = models.ForeignKey(Persona.run, null=false, blank=false)
    id_especialidad = models.ForeignKey(Especialidad.id_especialidad, null=false, blank=false)
    id_horario = models.ForeignKey(Horario.id_horario, null=false, blank=false)

#clase creada por matías (paciente)
class Paciente(models.Model):
    run = models.ForeignKey(Persona.run, null=false, blank=false)
    estado = models.BooleanField(default=true)