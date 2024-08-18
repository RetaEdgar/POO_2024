from bd import *

class Cliente:
    def __init__(self, nif, nombre, direccion,ciudad,tel):
        self.nif=nif
        self.nombre=nombre
        self.direccion=direccion
        self.ciudad=ciudad
        self.tel=tel
    def crear(self):
        try:
          cursor.execute(
            "insert into clienntes values(%s,%s,%s,%s,%s,%s);",
            (self.nif,self.nombre,self.direccion,self.ciudad,self.tel)
          )
          conexion.commit()
          return True
        except:
          return False
    @staticmethod
    def mostrar():
        try:
          cursor.execute(
            "select * from clientes",
            
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(nif,nombre,direccion,ciudad,tel):
       try:
         cursor.execute(
            "update clientes set nombre=%s, direccion=%s, ciudad=%s, tel=%s where nif=%s",
            (nombre,direccion,ciudad,tel,nif)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(nif):
        try:
          cursor.execute(
            "delete from clientes where nif=%s",
            (nif,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
    