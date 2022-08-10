"""
  7) realice una consulta al archivo data.py, muestre los items que no tienen colores 
  y ordenelos por nombre
"""
from data import *

items = Data.get_items()
#Aqui se guarda los items que no tienen colores y se ordena por nombre
items_sorted = []

for item in sorted(items, key=lambda item: item.get("name")):
    if item.get("color") == None:
        items_sorted.append(item)
        print(item.get("name"))

