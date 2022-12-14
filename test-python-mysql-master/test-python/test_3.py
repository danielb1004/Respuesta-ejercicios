"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""
from data import *

thirds = Data.get_thirds()

#Aqui se guarda el tercero ordenado por Nombre
thirds_sorted = []
for third in sorted(thirds, key=lambda third: third.get("tradename") if third.get("tradename") != '' else third.get("firstname") + ' ' + third.get("lastname") + ' ' + third.get("maidenname")):
    thirds_sorted.append(third)
    print(third.get("tradename") if third.get("tradename") != '' else third.get("firstname") + ' ' + third.get("lastname") + ' ' + third.get("maidenname"))

