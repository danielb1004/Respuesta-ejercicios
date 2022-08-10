"""
  10) realice una consulta al archivo data.py, muestre todos los terceros, reduzca la 
  información y solo muestre el nombre y la identificación, 
  ordenelos por identificación
"""
from tkinter import N
from data import *

thirds = Data.get_thirds()


for third in sorted(thirds, key=lambda third: third.get("identificationNumber")): 
  if third.get("firstname") != "":
    print(third.get("firstname") + " -- " + third.get("identificationNumber"))
  else:
    print(third.get("tradename") + " -- " + third.get("identificationNumber"))