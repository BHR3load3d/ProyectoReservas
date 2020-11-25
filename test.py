#import tablib # Librería soporte
from django.core.management.base import BaseCommand # Librería de comandos de Django

#from etl.admin import AssignmentResource # Import recurso de la aplicación

from AppMotorReservas.models import *
from AppMotorReservas.views import *
from datetime import datetime
import random

def llenadoSites():
    for i in range(10):
        s = Site()
        s.Identificador = "Site " + str(i)
        s.Direccion = "Dirección " + str(i)
        s.Numero = i * 10
        s.Piso = i
        s.CodPostal = '326' + str(i)
        s.save()
    pass

def llenadoEspacioTipo():
    for i in range(3):
        s = EspacioTipo()
        s.Descripcion = "Tipo " + str(i)
        s.save()
    pass

def llenadoReservasRestricciones():
    for i in range(1):
        s = ReservaRestricciones()
        s.Identificador = "Restricción " + str(i)
        s.TiempoReserva = 1
        s.UnidadTiempoReserva = 1 # 1: Horas
        s.AnticipacionMax = 7
        s.UnidadAnticipacionMax = 2 # 1: Horas, 2: Días
        s.save()
    pass

def llenadoEspacio():
    for i in range(20):
        s = Espacio()
        s.Descripcion = "Espacio " + str(i)
        s.RestriccionId = ReservaRestricciones.objects.get(id=1)
        s.Moneda = 1 # 1: Peso, 2: usd
        t = random.randrange(1, 3, 1)
        s.TipoId = EspacioTipo.objects.get(id=t) # va de 0 a 2
        s.Costo = random.uniform(1500.25, 5340.70)
        t2 = random.randrange(1,  10 , 1)
        s.SiteId = Site.objects.get(id=t2)
        s.save()
    pass

def llenadoMiembro():
    for i in range(3):
        s = Miembro()
        s.Nombre = "Miembro N° " + str(i)
        s.save()
    pass

def llenadoReservas():
    for i in range(3):
        t1 = datetime(2020, 11, i+1, i + 12, 0, 0, 0)
        t2 = datetime(2020, 11, i+3, i + 13, 0, 0, 0)
        EspacioId = Espacio.objects.get(id=i+1)
        MiembroId = Miembro.objects.get(id=i+1)

        s = Reserva.objects.create(FechaIni=t1, FechaFin=t2, EspacioId = EspacioId, MiembroId = MiembroId)

        s.save()
    pass 

def llenadobase():
    x = Site.objects.all()

    if x.count() == 0:
        print('Llenado de base de datos iniciado')

        llenadoSites()
        llenadoEspacioTipo()
        llenadoReservasRestricciones()
        llenadoEspacio()
        llenadoMiembro()
        llenadoReservas()

        print('Llenado de base de datos completo')

# Sólo se llama si no hay datos cargados
llenadobase()


# Prueba disponibilidad de espacios para una fecha y hora concreta
d1 = datetime(2020,11,3,14,0,0,0)
d2 = datetime(2020,11,5,15,0,0,0)

espacios = disponibilidadEspacios(1, d1, d2)

print('Cantidad de espacios que coinciden con la búsqueda: ' + str(espacios.count()))

for e in espacios:
    print(e)

# Prueba disponibilidad de fechas para un espacio en un rango de fechas y horas concretas
fechas = disponibilidadEspacio(1, '2020-11-01 00:00:00.0', '2020-11-05 15:00:00.0')

for f in fechas:
    print(f)

