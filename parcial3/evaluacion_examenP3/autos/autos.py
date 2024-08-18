from bd import *

class Auto:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.nif=nif
    def crear(self):
        try:
          cursor.execute(
            "insert into autos values(%s,%s,%s,%s,%s);",
            (self.matricula,self.marca,self.modelo,self.color,self.nif)
          )
          conexion.commit()
          return True
        except:
          return False
    @staticmethod
    def mostrar():
        try:
          cursor.execute(
            "select * from autos ",
            
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(matricula, marca, modelo, color, nif):
       try:
         cursor.execute(
            "update autos set marca=%s,modelo=%s,color=%s, nif=%s where matricula=%s",
            (marca,modelo,color,nif,matricula)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(matricula):
        try:
          cursor.execute(
            "delete from autos where matricula=%s",
            (matricula,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
    