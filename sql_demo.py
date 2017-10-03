import sqlite3
from random import randint

conn = sqlite3.connect('cine.db')

c = conn.cursor()

id_entrada = 1

##Configuración------------------------------------------------------------

#c.execute("DROP TABLE pelicula")
#c.execute("DROP TABLE funcion")
#c.execute("DROP TABLE cine")
#c.execute("DROP TABLE cinePelicula")
#c.execute("DROP TABLE funcionPelicula")
#c.execute("DROP TABLE entrada")

#c.execute("""CREATE TABLE pelicula (
#            id_pelicula text,
#            nombre_pelicula text
#
#     )""")

#c.execute("""CREATE TABLE funcion (
#            id_funcion text,
#            horario_funcion text
#
#     )""")

#c.execute("""CREATE TABLE cine (
#            id_cine text,
 #           nombre_cine text
 #    )""")

#c.execute("""CREATE TABLE cinePelicula (
#            id_cine text,
#            id_pelicula text
#
#     )""")

#c.execute("""CREATE TABLE funcionPelicula (
#            id_funcion text,
#            id_pelicula text
#
#     )""")

#c.execute("""CREATE TABLE entrada (
#            id_entrada text,
#            id_pelicula text,
#            id_cine text,
#            id_funcion text,
#            cant integer
#
#     )""")

#c.execute("INSERT INTO cine VALUES ('1', 'CinePlaneta')")
#c.execute("INSERT INTO cine VALUES('2','CineStark')")
#c.execute("SELECT * FROM cine")
#print(c.fetchall())

#c.execute("INSERT INTO funcion VALUES('1','16:00')")
#c.execute("INSERT INTO funcion VALUES('2','19:00')")
#c.execute("INSERT INTO funcion VALUES('3','20:00')")
#c.execute("INSERT INTO funcion VALUES('4','20:30')")
#c.execute("INSERT INTO funcion VALUES('5','21:00')")
#c.execute("INSERT INTO funcion VALUES('6','22:00')")
#c.execute("INSERT INTO funcion VALUES('7','23:00')")

#c.execute("SELECT * FROM funcion")
#print(c.fetchall())

#c.execute("INSERT INTO pelicula VALUES('1','IT')")
#c.execute("INSERT INTO pelicula VALUES('2','La Hora Final')")
#c.execute("INSERT INTO pelicula VALUES('3','Desaparecido')")
#c.execute("INSERT INTO pelicula VALUES('4','Deep El Pulpo')")
#c.execute("SELECT * FROM pelicula")
#print(c.fetchall())

#c.execute("INSERT INTO cinePelicula VALUES('1','1')")
#c.execute("INSERT INTO cinePelicula VALUES('1','2')")
#c.execute("INSERT INTO cinePelicula VALUES('1','3')")
#c.execute("INSERT INTO cinePelicula VALUES('1','4')")

#c.execute("INSERT INTO cinePelicula VALUES('2','3')")
#c.execute("INSERT INTO cinePelicula VALUES('2','4')")

#c.execute("SELECT * FROM cinePelicula")
#print(c.fetchall())

#c.execute("INSERT INTO funcionPelicula VALUES('1','4')")
#c.execute("INSERT INTO funcionPelicula VALUES('2','1')")
#c.execute("INSERT INTO funcionPelicula VALUES('3','3')")
#c.execute("INSERT INTO funcionPelicula VALUES('3','4')")
#c.execute("INSERT INTO funcionPelicula VALUES('4','1')")
#c.execute("INSERT INTO funcionPelicula VALUES('5','2')")
#c.execute("INSERT INTO funcionPelicula VALUES('5','3')")
#c.execute("INSERT INTO funcionPelicula VALUES('6','1')")
#c.execute("INSERT INTO funcionPelicula VALUES('7','3')")


#c.execute("SELECT * FROM funcionPelicula")
#print(c.fetchall())

##---------------------------------------------------------------------------

def listarCine():
	c.execute("SELECT * FROM cine")
	return c.fetchall()

def listarPrueba():
	c.execute("SELECT * FROM cinePelicula")
	return c.fetchall()

def listarPeliculas(id_cine):
	c.execute("SELECT cp.id_pelicula, p.nombre_pelicula FROM cinePelicula cp JOIN pelicula p ON cp.id_pelicula = p.id_pelicula where id_cine=:id_cine",{'id_cine': id_cine})
	return c.fetchall()

def listarFunciones(id_pelicula):
	c.execute("SELECT * FROM funcionPelicula where id_pelicula=:id_pelicula",{'id_pelicula': id_pelicula})
	return c.fetchall()

def generarEntrada(id_pelicula,id_cine,id_funcion,cant):
	id_entrada += 1 
	with conn:
		c.execute("INSERT INTO entrada VALUES(?, ?, ?, ?, ?)", (id_entrada,id_pelicula,id_cine,id_funcion,cant))
		conn.commit()


#conn.close()
