# Generar scripts que realicen las siguientes consultas

-------* Consultar los items que pertenezcan a la compañia (utilizando INNER JOIN) con ID #3 *-------
SELECT * FROM companies INNER JOIN items ON items.id = 3

-------* Mostrar los últimos 10 items *-------

SELECT * FROM items ORDER BY id DESC LIMIT 10;
-------* Mostrar los items que en el nombre terminen con la letra A *-------


-------* Mostrar los items que tengan relacionado el color Rojo *-------
select * from items where name like "%a";
