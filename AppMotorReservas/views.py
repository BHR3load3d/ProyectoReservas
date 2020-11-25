from django.shortcuts import render
from django.http import HttpResponse

from .models import Site, EspacioTipo, ReservaRestricciones, Espacio, Miembro, Reserva
import random
from datetime import datetime, timedelta
from collections import deque

# La view
def disponibilidad(request, tipo, entidad_id, start_date, end_date):
    if tipo == 1:
         d = disponibilidadEspacios(entidad_id, start_date, end_date) # entidad_id: site_id
    else:
        d = disponibilidadEspacio(entidad_id, start_date, end_date) # entidad_id: espacio_id

    return HttpResponse(d)

# Método que retorna los espacios disponibles según el rango de fecha y hora
def disponibilidadEspacios(site_id, start_date, end_date):
    site = Site.objects.get(pk = site_id)

    espaciostipo = EspacioTipo.objects.filter(Activo=True)

    espacios_id = Reserva.objects.exclude(FechaIni__gt = end_date).exclude(FechaFin__lt = start_date).values_list('EspacioId', flat=True).distinct()
    espacios = Espacio.objects.filter(SiteId = site).filter(TipoId__in = espaciostipo).exclude(id__in = espacios_id)


    return espacios

# Método que retorna los espacios disponibles según el rango de fecha y hora
def disponibilidadEspacio(espacio_id, start_date, end_date):
    restriccion = Espacio.objects.get(pk = espacio_id).RestriccionId
    tiempoReserva = restriccion.TiempoReserva

    start_date_dt = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')

    reservas = Reserva.objects.filter(EspacioId = espacio_id).exclude(FechaIni__lt = start_date_dt).exclude(FechaFin__gt = end_date_dt).values_list('FechaIni', flat=True)

    print('.............................................................................................')
    print("Reservas encontradas para el espacio:")
    for r in reservas:
        print(r)
    print('.............................................................................................')
    x = end_date_dt-start_date_dt
    y = int((x.days*24) + (x.seconds/60/60)) # Cantidad de horas que hay entre las dos fechas
    z = int(y / tiempoReserva) # la distancia entre reservas (tiempo de reserva esta en HS) - cantidad de reservas

    fechas = deque([])

    for i in range(0, y + 1, 1): #Le sumo 1 para que incluya end_date
        f = start_date_dt + timedelta(hours=i)
        b = False

        for r in reservas:
            if r.year == f.year and r.day == f.day and r.month == f.month and r.hour == f.hour and r.minute == f.minute and r.second == f.second:
                b = True
        
        if b == False:
            fechas.append(f)

    return fechas