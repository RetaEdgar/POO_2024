from funcones import *
from autos import autos
import getpass
from usurios import usuario
from clientes import cliente
from revisiones import revision


def menu_principal():
    while True:    
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            #Agregar codigo
            obj_usurio=usuario.Usuario(nombre,apellidos,email,password)
            resultado=obj_usurio.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...")  
            esperarTecla()      
        elif opcion == '2' or opcion=="LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo 
            registro=usuario.Usuario.iniciar_sesion(email,password)
            if registro:
                menu_inicial()
            else:
                print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                esperarTecla()    
        elif opcion == '3' or opcion=="SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            #opc=False
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_inicial():
    while True:
        borrarPantalla()
        print("""
.:: Menu principal::.
              1.- Clientes
              2.- Autos
              3.- Revisiones
              4.- Salir""")
        opcion_inicial=input("Selecciona una de las opciones anteriores:").upper()
        if opcion_inicial=="1" or opcion_inicial=="CLIENTES":
            menu_clientes()
        elif opcion_inicial=="2" or opcion_inicial=="AUTOS":
            menu_autos()
        elif opcion_inicial =="3" or opcion_inicial=="REVISIONES":
            menu_revision()
        elif opcion_inicial=="4" or opcion_inicial=="SALIR":
            break

def menu_revision():
    while True:
        borrarPantalla()
        print("""
    .::Menu de Revisiones::.
            1.- Crear
            2.- mostrar
            3.- actualizar
            4.- eliminar
            5.- Salir""")
        opcion= input("Selecciona una de las opciones anteriores").upper()
        
        if opcion=='1' or opcion=="CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Revision ::. ")
            no_revision=input("\t Numero de Revision: ")
            cambiofiltro=input("\t Cambio de Filtro s/n: ")
            cambioaceite=input("\t Cambio Aceite s/n:")
            cambiofreno=input("\t Cambio de Frenos s/n:")
            otros=input("\t Otros:")
            matricula=input("\t Matricula:")
            #Agregar codigo
            obj_revision=revision.Revision(no_revision,cambiofiltro,cambioaceite,cambiofreno,otros,matricula)
            resultado=obj_revision.crear()
            if resultado:
                print(f"\n \t \t.::La Revision se creo Correctamente ::.")
            else:
                print(f"\n \t \t No fue posible crear la revision... vuelva a intentarlo...") 
            esperarTecla()
            
        elif opcion=='2' or opcion =="MOSTRAR":
            borrarPantalla()
            #Agregar codigo  
            registros=revision.Revision.mostrar()
            if len(registros)>0:
                num_notas=1
                for fila in registros:
                   print(f"\n Numero de Revision: {fila[0]}   .- Cambio Filtro: {fila[1]}         .- Cambio Aceite: {fila[2]} \t Cambia Freno: {fila[3]}  \t Otros{fila[4]} Matricula {fila[5]}") 
                   num_notas+=1    
            else:
                print(f"\n \t \t** No existen registros para el usuario ... vuelva a intentarlo **...")
            esperarTecla()
            
        elif opcion=='3' or opcion=="ACTUALIZAR":
            borrarPantalla()
            no_revision=input("\t Numero de revision:")
            cambiofiltro=input("\t Cambio de Filtro s/n: ")
            cambioaceite=input("\t Cambio Aceite s/n:")
            cambiofreno=input("\t Cambio de Frenos s/n:")
            otros=input("\t Otros:")
            matricula=input("\t Matricula:")
             #Agregar codigo
            resultado=revision.Revision.actualizar(no_revision,cambiofiltro,cambioaceite,cambiofreno,otros , matricula)
            if resultado:
                print(f"\n \t \t.::revision Actualizada Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible actualizar la revision ... vuelva a intentarlo **...")  
            esperarTecla()
            
        elif opcion=='4' or opcion=="ELIMINAR":
            no_revision= input("\t \t Numero de revision a eliminar:")
            #Agregar codigo
            resultado=revision.Revision.eliminar(no_revision)
        elif opcion=='5' or opcion=="SALIR":
            print("\t !!Gracias por usar nuestro software¡¡")

            break
        else:
            print("Asegurate que la opcion sea la correcta")


def menu_clientes():
    while True:
        borrarPantalla()
        print("""
    .::Menu de Clientes::.
            1.- Crear
            2.- mostrar
            3.- actualizar
            4.- eliminar
            5.- Salir""")
        opcion= input("Selecciona una de las opciones anteriores").upper()
        
        if opcion=='1' or opcion=="CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Auto ::. ")
            nif=input("\t nif: ")
            nombre=input("\t Nombre: ")
            direccion=input("\t Direccion:")
            ciudad=input("\t Ciudad:")
            tel=input("\t Tel:")
            #Agregar codigo
            obj_cliente=cliente.Cliente(nif,nombre,direccion,ciudad,tel)
            resultado=obj_cliente.crear()
            if resultado:
                print(f"\n \t \t.::El cliente se creo Correctamente ::.")
            else:
                print(f"\n \t \t No fue posible crear el cliente... vuelva a intentarlo...") 
            esperarTecla()
            
        elif opcion=='2' or opcion =="MOSTRAR":
            borrarPantalla()
            #Agregar codigo  
            registros=cliente.Cliente.mostrar()
            if len(registros)>0:
                num_notas=1
                for fila in registros:
                   print(f"\n Nif: {fila[0]}   .- Nombre: {fila[1]}         Direccion: {fila[2]} \t Ciudad: {fila[3]}  \t Tel{fila[4]}") 
                   num_notas+=1    
            else:
                print(f"\n \t \t** No existen clientes  ... vuelva a intentarlo **...")
            esperarTecla()
            
        elif opcion=='3' or opcion=="ACTUALIZAR":
             borrarPantalla()
             nombre= input("\t \t Nombre: ")
             direccion= input("\t Direccion: ")
             ciudad= input("\t Nueva Ciudad: ")
             tel=input("\t Nuevo Telefono:")
             #Agregar codigo
             resultado=cliente.Cliente.actualizar(nombre, direccion, ciudad,tel)
             if resultado:
                 print(f"\n \t \t.::Cliente Actualizado Correctamente ::.")
             else:
                print(f"\n \t \t** No fue posible actualizar al cliente ... vuelva a intentarlo **...")  
             esperarTecla()
            
        elif opcion=='4' or opcion=="ELIMINAR":
            nif= input("\t \t Nif del cliente a eliminar: ")
            #Agregar codigo
            resultado=cliente.Cliente.eliminar(nif)
            esperarTecla()
        elif opcion=='5' or opcion=="SALIR":
            print("\t !!Gracias por usar nuestro software¡¡")
            break
        else:
            print("Asegurate que la opcion sea la correcta")

def menu_autos():
    while True:
        borrarPantalla()
        print("""
    .::Menu de autos::.
            1.- Crear
            2.- mostrar
            3.- actualizar
            4.- eliminar
            5.- Salir""")
        opcion= input("Selecciona una de las opciones anteriores").upper()
        
        if opcion=='1' or opcion=="CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Auto ::. ")
            matricula=input("\t 1Matricula: ")
            marca=input("\t Marca: ")
            modelo=input("\t modelo:")
            color=input("\t Color:")
            nif=input("\t Nif:")
            #Agregar codigo
            obj_nota=autos.Auto(matricula,marca,modelo,color,nif)
            resultado=obj_nota.crear()
            if resultado:
                print(f"\n \t \t.::El Auto se creo Correctamente ::.")
            else:
                print(f"\n \t \t No fue posible crear el auto... vuelva a intentarlo...") 
            esperarTecla()
            
        elif opcion=='2' or opcion =="MOSTRAR":
            borrarPantalla()
            #Agregar codigo  
            registros=autos.Auto.mostrar()
            if len(registros)>0:
                num_notas=1
                for fila in registros:
                   print(f"\nMatricula: {fila[0]}   .- marca: {fila[1]}         Modelo: {fila[2]} \tColor: {fila[3]}") 
                   num_notas+=1    
            else:
                print(f"\n \t \t** No existen Autos ... vuelva a intentarlo **...")
            esperarTecla()
            
        elif opcion=='3' or opcion=="ACTUALIZAR":
             borrarPantalla()
             marca= input("\t \t Marca: ")
             modelo= input("\t Nuevo modelo: ")
             color = input("\t Nuevo Color: ")
             nif=input("\t Nuevo Nif:")
             #Agregar codigo
             resultado=autos.Auto.actualizar(marca, modelo, color,nif)
             if resultado:
                 print(f"\n \t \t.::Auto Actualizadp Correctamente ::.")
             else:
                print(f"\n \t \t** No fue posible actualizar el Auto ... vuelva a intentarlo **...")  
             esperarTecla()
            
        elif opcion=='4' or opcion=="ELIMINAR":
            matricula= input("\t \t Matricula del auto a eliminar: ")
            #Agregar codigo
            resultado=autos.Auto.eliminar(matricula)
        elif opcion=='5' or opcion=="SALIR":
            print("\t !!Gracias por usar nuestro software¡¡")

            break
        else:
            print("Asegurate que la opcion sea la correcta")

if __name__ == "__main__":
  menu_principal()