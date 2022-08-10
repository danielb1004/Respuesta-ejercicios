"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales por su id, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
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

    

def get_branch_by_id(id):
  for branch in branches:
    if branch.get("id") == id:
      return branch
  return None


#aqui se ejecuta la funcion con el id 1 
print(get_branch_by_id(1))