from bd import *

class Revision:
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofreno, otros, matricula):
        self.no_revision=no_revision
        self.cambiofiltro=cambiofiltro
        self.cambioaceite=cambioaceite
        self.cambiofreno=cambiofreno
        self.otros=otros
        self.matricula=matricula
    def crear(self):
        try:
          cursor.execute(
            "insert into autos values(%s,%s,%s,%s,%s,%s);",
            (self.no_revision,self.cambiofiltro,self.cambioaceite,self.cambiofreno,self.otros,self.matricula)
          )
          conexion.commit()
          return True
        except:
          return False
    @staticmethod
    def mostrar():
        try:
          cursor.execute(
            "select * from revisiones ",
            
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(no_revision,cambiofiltro,cambioaceite,cambiofreno,otros,matricula):
       try:
         cursor.execute(
            "update revisiones set cambiofiltro=%s,cambioaceite=%s, cambiofreno=%s, otros=%s, matricula=%s where no_revision=%s",
            (cambiofiltro,cambioaceite,cambiofreno,otros,matricula,no_revision)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(no_revision):
        try:
          cursor.execute(
            "delete from revisiones where no_revision=%s",
            (no_revision,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
    