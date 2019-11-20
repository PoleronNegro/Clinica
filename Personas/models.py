from django.db import models
from Detalle import models as detalleModelo


"""importacion realizada por oscar"""
# Create your models here.

#clase creada por matías (persona)
class Persona(models.Model):
    #realice una actualizacion de datos Oscar Torres
    run = models.CharField(primary_key=True,max_length=10, null=False, blank=False)
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    #columna genero añadida por oscar
    idgenero = models.ForeignKey(detalleModelo.Genero,on_delete = models.CASCADE)
    telefono = models.CharField(max_length=12,null=False, blank=False)
    correo = models.EmailField(max_length=45, null=False, blank=False)
    direccion = models.CharField(max_length=30, null=False, blank=False)
 #columna comuna añadida por oscar
    idcomuna = models.ForeignKey(detalleModelo.Comuna,on_delete = models.CASCADE)

#clase creada por matías (medico)
class Medico(models.Model):
    run = models.OneToOneField(Persona,on_delete = models.CASCADE)
    idespecialidad = models.ForeignKey(detalleModelo.Especialidad,on_delete = models.CASCADE)
    id_horario = models.ForeignKey(detalleModelo.Horario,on_delete = models.CASCADE)

#clase creada por matías (paciente)
class Paciente(models.Model):
    run = models.OneToOneField(Persona,on_delete = models.CASCADE)
    estado = models.BooleanField(default=True)

#modificado por oscar
class Hora_Medica(models.Model):
    idmedico = models.ForeignKey(Medico,on_delete = models.CASCADE)
    fecha_hora = models.DateTimeField()
    idprevision = models.ForeignKey(detalleModelo.Prevision,on_delete = models.CASCADE)
    idestado = models.ForeignKey(detalleModelo.Estado,on_delete = models.CASCADE)
    idpersona = models.ForeignKey(Paciente,on_delete = models.CASCADE)