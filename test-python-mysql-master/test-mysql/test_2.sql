# Generar scripts que realicen las siguientes modificaciones

-------* Colocarle el Precio a los items que lo tengan en NULL, tomando como referencia el valor del costo del item + 10.000 *-------
 update items set price = cost + "10000" where price = 0;

-------* Incrementar el precio de los items en 10% *-------

update items set price = price * 0.10 + price;
-------* Anteponer la palabra Nuevo a los items que comiencen con C en el nombre *-------

 update items set name = ("nuevo")+name where name like "c%";