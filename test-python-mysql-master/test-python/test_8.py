"""
  8) realice una consulta al archivo data.py, muestre los items que si tienen colores, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente
"""
from data import *

items = Data.get_items()
colors = Data.get_colors()
#Aqui se guarda los items que tienen colores y se ordena por nombre
items_sorted = []

for item in sorted(items, key=lambda item: item.get("name")):
    if item.get("color") != None:
      for color in colors:
        if item.get("color") == color.get("colorCode"):
          item.update({"colorName": color.get("colorName")})
          items_sorted.append(item)
          print(item.get("name"), " - ", item.get("color"))



    