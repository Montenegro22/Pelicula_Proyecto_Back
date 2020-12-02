import mysql.connector
from mysql.connector import errorcode
from modelos import Pelicula

class Dao:

    def add_pelicula(self,pelicula):
#METODO CREAR PELICULA
        try:
            conn = mysql.connector.connect(user='Pelicula', password='Nat.2008', database='Pelicula', host='127.0.0.1')
            cursor = conn.cursor()
            sql = ("INSERT INTO Peliculas (id, Nombre, Genero, Año, Productora, Pais, Duracion, Idiomas, Descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            val = (pelicula.id, pelicula.Nombre, pelicula.Genero, pelicula.Año, pelicula.Productora, pelicula.Pais, pelicula.Duracion, pelicula.Idiomas, pelicula.Descripcion)
            cursor.execute(sql,val)
            conn.commit()
            cursor.close()
            conn.close()
            return True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print ("Por favor verifique  ")
          #  elif err.errno == errorcode.ER_BAD_BD_ERROR:
           #     print ("La base de datos a la que desea acceder no existe, por favor verificar conexion")
            else:
                print (err)             
            return False     




    def consultar_pelicula(self,id):
            #METODO CONSULTAR PELICULA

        try:
            conn = mysql.connector.connect(user='Pelicula', password='Nat.2008', database='Pelicula', host='127.0.0.1')
            cursor = conn.cursor()
            sql = ("SELECT * FROM Peliculas WHERE id = "+str(id))       
            cursor.execute(sql)
            data = cursor.fetchone()
            pelicula = None
            if data is not None:
                pelicula = Pelicula(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
            cursor.close()
            conn.close()
            return pelicula
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print ("Por favor verifique  ")
        #    elif err.errno == errorcode.ER_BAD_BD_ERROR:
         #       print ("La base de datos a la que desea acceder no existe, por favor verificar conexion")
            else:
                print (err)             
            return None     


    def actualizar_pelicula(self,pelicula):
#METODO ACTUALIZAR PELICULA
        try:
            conn = mysql.connector.connect(user='Pelicula', password='Nat.2008', database='Pelicula', host='127.0.0.1')
            cursor = conn.cursor()
            sql = ("update Peliculas set Nombre=%s, Genero=%s, Año=%s, Productora=%s, Pais=%s, Duracion=%s, Idiomas=%s, Descripcion=%s where id=%s;" )    
            val = (pelicula.id,pelicula.Nombre, pelicula.Genero, pelicula.Año, pelicula.Productora, pelicula.Pais, pelicula.Duracion, pelicula.Idiomas, pelicula.Descripcion)
            cursor.execute(sql,val)
            cursor.close()
            conn.close()
            return True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print ("Por favor verifique  ")
            #elif err.errno == errorcode.ER_BAD_BD_ERROR:
             #   print ("La base de datos a la que desea acceder no existe, por favor verificar conexion")
            else:
                print (err)             
            return False    

    def eliminar_pelicula(self,pelicula):
    #METODO ELIMINAR PELICULA
        try:
            conn = mysql.connector.connect(user='Pelicula', password='Nat.2008', database='Pelicula', host='127.0.0.1')
            cursor = conn.cursor()
            sql = ("DELETE FROM peliculas WHERE id = %s;")       
            cursor.execute(sql,(id))
            cursor.close()
            conn.close()
            return True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print ("Por favor verifique  ")
            #elif err.errno == errorcode.ER_BAD_BD_ERROR:
             #   print ("La base de datos a la que desea acceder no existe, por favor verificar conexion")
            else:
                print (err)             
            return False 


    def listar_pelicula(self):
            #METODO LISTAR PELICULA 
        try:
            conn = mysql.connector.connect(user='Pelicula', password='Nat.2008', database='Pelicula', host='127.0.0.1')
            cursor = conn.cursor()
            sql = ("SELECT * FROM peliculas")       
            cursor.execute(sql)
            peliculas = []
            for fila in cursor:
                pelicula = Pelicula(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8]) 
                peliculas.append(pelicula)
            cursor.close()
            conn.close()
            return peliculas

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print ("Por favor verifique  ")
            #elif err.errno == errorcode.ER_BAD_BD_ERROR:
             #   print ("La base de datos a la que desea acceder no existe, por favor verificar conexion")
            else:
                print (err)             
            return None 
