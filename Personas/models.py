from django.db import models
#importacion realizada por oscar
from Detalle import models as detalleModelo
# Create your models here.

#clase creada por matías (persona)
class Persona(models.Model):
    run = modesl.CharField(max_length=10, null=false, blank=false)
    nombre = modesl.CharField(max_length=30, null=false, blank=false)
    apellido = modesl.CharField(max_length=30, null=false, blank=false)
    telefono = modesl.CharField(max_length=12, null=false, blank=false)
    correo = modesl.CharField(max_length=45, null=false, blank=false)
    direccion = modesl.CharField(max_length=30, null=false, blank=false)

#clase creada por matías (medico)
class Medico(models.Model):
    run = models.ForeignKey(Persona.run, null=false, blank=false)
    id_especialidad = models.ForeignKey(Especialidad.id_especialidad, null=false, blank=false)
    id_horario = models.ForeignKey(Horario.id_horario, null=false, blank=false)

#clase creada por matías (paciente)
class Paciente(models.Model):
    run = models.ForeignKey(Persona.run, null=false, blank=false)
    estado = models.BooleanField(default=true)