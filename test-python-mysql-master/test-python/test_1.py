""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""
from data import *

#Aqui se guarda las empresas
companies = Data.get_companies()
#Aqui se guarda las sucursales
branches = Data.get_branches()
#Aqui se guarda el resultado
companies_branches = {}
for company in companies:
  companies_branches[company.get("name")] = []
  for branch in company.get("branches"):
    for b in branches:
      if b.get("id") == branch:
        companies_branches[company.get("name")].append(b.get("name"))

    

print(companies_branches)




