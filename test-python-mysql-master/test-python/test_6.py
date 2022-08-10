"""
  6) ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a terner todos los terceros que pertenezcan a esa compañia
"""

from data import *

thirds = Data.get_thirds()
companies = Data.get_companies()

#Aqui se guarda la compañia ordenado por nombre
companies_sorted = []
for company in sorted(companies, key=lambda company: company.get("name")):
    companies_sorted.append(company)
    print(company.get("name"))
    #Aqui se guarda el tercero ordenado por nombre 
    thirds_sorted = []
    for third in sorted(thirds, key=lambda third: third.get("tradename") if third.get("tradename") != '' else third.get("firstname") + ' ' + third.get("lastname") + ' ' + third.get("maidenname")):
        if third.get("companyid") == company.get("id"):
            thirds_sorted.append(third)
            print(third.get("tradename") if third.get("tradename") != '' else third.get("firstname") + ' ' + third.get("lastname") + ' ' + third.get("maidenname"))
    company.update({"thirds": thirds_sorted})
    print("")
