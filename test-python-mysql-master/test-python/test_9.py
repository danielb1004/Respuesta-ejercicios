"""
9) realice una consulta al archivo data.py, muestre todos los items, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente,
  en caso de que esté lo tenga. 
  
  El resultado del ordenando debe ser así, en la parte inicial los items 
  que no tienen color y en la parte final los que si tienen color, todo dentro de
  un mismo objeto
"""
from data import *

items = Data.get_items()
colors = Data.get_colors()
#Aqui se guarda los items 
items_sorted = []
items_sorted_color = []
for item in sorted(items, key=lambda item: item.get("name")): 
  #Aqui se guarda los items que no tienen color
  if item.get("color") == None:
    items_sorted.append(item)
  #Aqui se guarda los items que tienen color
  else:
    items_sorted.append(item)
    for color in colors:
      if color.get("id") == item.get("color"):
        item["color"] = color.get("name")
        break
for item in sorted(items_sorted, key=lambda item: item.get("color") if item.get("color") != None else "No tiene color"): 
  if item.get("color") == None:
    items_sorted_color.append(item)
    print(item.get("name"), "No tiene color")

for item in sorted(items_sorted, key=lambda item: item.get("color") if item.get("color") != None else "No tiene color"): 
  if item.get("color") != None:
    items_sorted_color.append(item)
    print(item.get("name"), item.get("color"))
    
print(items_sorted_color)
