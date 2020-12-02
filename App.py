#!/usr/bin/python3
#CONTROLADOR
import mysql.connector
from mysql.connector import errorcode
import cgi
import os
from Dao import Dao
from modelos import Pelicula
import json


print ('Content-Type: text/json')
print ('')


datos= cgi.FieldStorage()
dao = Dao()
if os.environ['REQUEST_METHOD']=="POST":

   id=datos.getvalue('id')
   Nombre=datos.getvalue('Nombre')
   Genero=datos.getvalue('Genero')
   Año=datos.getvalue('Anio')
   Productora = datos.getvalue('Productora')
   Pais = datos.getvalue('Pais')
   Duracion = datos.getvalue('Duracion')
   Idiomas = datos.getvalue('Idiomas')
   Descripcion = datos.getvalue('Descripcion')

   if dao.consultar_pelicula(id) is not None:
      print(json.dumps('{"mensaje":"Esa película ya existe"}'))
   else:
      pelicula = Pelicula(id,Nombre,Genero,Año,Productora,Pais,Duracion,Idiomas,Descripcion)
      
      if dao.add_pelicula(pelicula):
         print('{"mensaje":"Pelicula creada"}')
      else:
         print('{"mensaje":"Error al crear pelicula"}')   


elif os.environ['REQUEST_METHOD']=="PUT":
#ACTUALIZAR

   id=datos.getvalue('id')
   Nombre=datos.getvalue('Nombre')
   Genero=datos.getvalue('Genero')
   Año=datos.getvalue('Anio')
   Productora = datos.getvalue('Productora')
   Pais = datos.getvalue('Pais')
   Duracion = datos.getvalue('Duracion')
   Idiomas = datos.getvalue('Idiomas')
   Descripcion = datos.getvalue('Descripcion')

   if dao.consultar_pelicula(id) is None:
      print(json.dumps('{"mensaje":"Esa película YA existe"}'))
   else:
      pelicula = Pelicula(id,Nombre,Genero,Año,Productora,Pais,Duracion,Idiomas,Descripcion)
      
      if dao.actualizar_pelicula(pelicula):
         print('{"mensaje":"La pelicula ha sido actualizada"}')
      else:
         print('{"mensaje":"Error al actualizar pelicula"}')   


elif os.environ['REQUEST_METHOD']=="DELETE":
#ELIMINAR

   id=datos.getvalue('id')


   if dao.consultar_pelicula(id) is None:
      print(json.dumps("{'mensaje':'Esa película no existe'}"))
   else:
      pelicula = Pelicula(id,Nombre,Genero,Año,Productora,Pais,Duracion,Idiomas,Descripcion)
      
      if dao.eliminar_pelicula(pelicula):
         print("{'mensaje':'La pelicula se ha eliminado'}")
      else:
         print("{'mensaje':'Error al eliminar pelicula'}")   


elif os.environ['REQUEST_METHOD']=="GET":
#LISTAR
   
   dao=Dao()
   peliculas = dao.listar_pelicula()
   print("[")
   longitud=len(peliculas)
   i=1
   for pelicula in peliculas:
      print(json.dumps(pelicula.dict))
      if i<longitud:
         print(",")
         i=i+1
   print("]") 