from django.db import models
from datetime import datetime, timedelta
from django.utils.translation import ugettext as _

class Site(models.Model):
    Identificador = models.CharField(max_length=255)
    Direccion =  models.CharField(max_length=255)
    Numero = models.IntegerField()
    Piso = models.IntegerField()
    CodPostal =  models.CharField(max_length=25)
    # Ciudad =  models.CharField(max_length=255)
    # Provincia =  models.CharField(max_length=255)
    # Pais =  models.CharField(max_length=255)
    Activo = models.BooleanField(default=True)

class EspacioTipo(models.Model):
    Descripcion = models.CharField(max_length=512)
    #otros atributos útiles que permitan un filtrado
    Activo = models.BooleanField(default=True)

class ReservaRestricciones(models.Model):
    Identificador = models.CharField(max_length=255)
    TiempoReserva = models.IntegerField()
    UnidadTiempoReserva = models.IntegerField()
    AnticipacionMax = models.IntegerField()
    UnidadAnticipacionMax = models.IntegerField()
    Activo = models.BooleanField(default=True)

class Espacio(models.Model):
    SiteId = models.ForeignKey(Site, on_delete=models.CASCADE)
    RestriccionId = models.ForeignKey(ReservaRestricciones, on_delete=models.CASCADE)
    Descripcion =  models.CharField(max_length=255)
    TipoId = models.ForeignKey(EspacioTipo, on_delete=models.CASCADE)
    Costo = models.FloatField()
    Moneda = models.IntegerField()
    Activo = models.BooleanField(default=True)
    class Meta:
        verbose_name = _('Espacio')
        verbose_name_plural = _('Espacios')

    def __str__(self):
        return self.Descripcion 
    
    def Estado(self):
        #fecha = datetime.now()
        fecha = datetime(2020,11,1,0,0,0,0) #para las pruebas. queda el datetime.now()
        r = Reserva.objects.filter(EspacioId = self.id).filter(FechaIni__date = datetime(fecha.year,fecha.month,fecha.day).date())
        return r

class Miembro(models.Model): #dummy a efectos del desarrollo, entiendo que ya tenes esta tabla
    Nombre = models.CharField(max_length=255)

class Reserva(models.Model):
    EspacioId = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    MiembroId = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    FechaIni = models.DateTimeField()
    FechaFin = models.DateTimeField()
    FechaAlta = models.DateTimeField(auto_now=True)
    Activo = models.BooleanField(default=True)



