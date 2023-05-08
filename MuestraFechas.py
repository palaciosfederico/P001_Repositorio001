# El programa devuelve fecha actual
# Modulos a utilizar
import os
from datetime import datetime

# Definición de variables
# Varibles tipo Time
# FechaActual

# -------- Inicio de Programa --------

FechaActual=datetime.now()

DiaActual=FechaActual.day
MesActual=FechaActual.month
AñoActual=FechaActual.year

HoraActual=FechaActual.hour
MinutoActual=FechaActual.minute
SegundoActual=FechaActual.second


print('Fecha Actual: %s: ' %(FechaActual))
print("Día %s - Mes %s - Año %s" %(DiaActual,MesActual,AñoActual) )
print("Hora:%s Minutos:%s Segundos:%s" %(HoraActual,MinutoActual,SegundoActual) )


# Fin Archivo