#Creado por Oscar
from django.db import models
#importacion realizada por oscar
from Personas import models as modelopersonas

# Create your models here.

#modificado por oscar
class Genero (models.Model):
    detalle = models.CharField(max_length=15,null=False,blank=False)

#modificado por oscar
class Especialidad (models.Model):
    nombre = models.CharField(max_length=30,null=False,blank=False)

#modificado por oscar
class Region (models.Model):
    nombre_region = models.CharField(max_length=64,null=False,blank=False)
    num_regional = models.CharField(max_length=3,null=False,blank=False)

#modificado por oscar
class Provincia (models.Model):
    nombre_provincia = models.CharField(max_length=64,null=False,blank=False)
    id_region = models.ForeignKey(Region,on_delete = models.CASCADE)

#modificado por oscar
class Comuna (models.Model):
    nombre_provincia = models.CharField(max_length=64,null=False,blank=False)
    id_provincia = models.ForeignKey(Provincia,on_delete = models.CASCADE)

#modificado por oscar
class Prevision (models.Model):
    nombre = models.CharField(max_length=30,null=False,blank=False)
    tipo = models.CharField(max_length=15,null=False,blank=False)

class Horario (models.Model):
    Inicio = models.DateTimeField()