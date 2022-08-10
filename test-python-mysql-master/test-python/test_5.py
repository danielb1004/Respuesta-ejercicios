"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""
from data import *

thirds = Data.get_thirds()
companies = Data.get_companies()
#Aqui se guarda el tercero ordenado por nombre 
thirds_sorted = []
for third in sorted(thirds, key=lambda third: third.get("tradename") if third.get("tradename") != '' else third.get("firstname") + ' ' + third.get("lastname") + ' ' + third.get("maidenname")):
    thirds_sorted.append(third)
    for company in companies:
        if third.get("companyid") == company.get("id"):
            third.update({"company": company.get("name")})
            print(third.get("tradename") if third.get("tradename") != '' else third.get("firstname") + ' ' + third.get("lastname") + ' ' + third.get("maidenname"), " - ", third.get("company"))
