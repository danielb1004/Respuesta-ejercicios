"""
  4) ordenar los terceros que se tienen en el archivo data.py por identificationNumber
"""

from data import *

thirds = Data.get_thirds()

#Aqui se guarda el tercero ordenado por identificationNumber
thirds_sorted = []
for third in sorted(thirds, key=lambda third: third.get("identificationNumber")):
    thirds_sorted.append(third)
    print(third.get("identificationNumber"))