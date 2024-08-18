# from clientes import cliente
# from planes import plan
# from empleados import empleados
# from usuarios import usuario
# from servicios import servicio
# import getpass
# from funciones import *



# def menu_InicioSesion():
#     while True:    
#         borrarPantalla()
#         print("""
#       .::  Inicio de sesion ::. 
#           1.- Registro
#           2.- Login
#           3.- Salir 
#           """)
#         opcion = input("\t Elige una opción: ").upper()

#         if opcion == '1' or opcion=="REGISTRO":
#             borrarPantalla()
#             print("\n \t ..:: Registro en el Sistema ::..")
#             nombre=input("\t ¿Cual es tu nombre?: ")
#             apellidos=input("\t ¿Cuales son tus apellidos?: ")
#             email=input("\t Ingresa tu email: ")
#             password=getpass.getpass("\t Ingresa tu contraseña: ")
#             #Agregar codigo
#             obj_usurio=usuario.Usuario(nombre,apellidos,email,password)
#             resultado=obj_usurio.registrar()
#             if resultado:
#                 print(f"\n\t {nombre} {apellidos}, se registro correctamente, con el email: {email}")
#             else:
#                 print(f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...")  
#             esperarTecla()      
#         elif opcion == '2' or opcion=="LOGIN":
#             borrarPantalla()
#             print("\n \t ..:: Inicio de Sesión ::.. ")     
#             email=input("\t Ingresa tu E-mail: ")
#             password=getpass.getpass("\t Ingresa tu Contraseña: ")
#             #Agregar codigo 
#             registro=usuario.Usuario.iniciar_sesion(email,password)
#             if registro:
#                 menu_inicial()
#             else:
#                 print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
#                 esperarTecla()    
#         elif opcion == '3' or opcion=="SALIR":
#             print("\n\t.. ¡Gracias Bye! ...")
#             #opc=False
#             break
#             #exit()
#         else:
#             print("\n \t \t Opción no válida. Intenta de nuevo.")
#             esperarTecla

# def menu_inicial():
#     while True:
#         borrarPantalla()
#         print("""
#             ..::Menu Principal::..
#             1.- Cliente...
#             2.-Empleado...
#             3.- Salir""")
#         opcion=input("Selecciona una de las opciones:").upper()
#         if opcion=='1' or opcion =='CLIENTE':
#             menu_clientes()
#         if opcion=='2' or opcion =='EMPLEADO':
#             jaja=input("Coloca la contraseña para poder acceder: ")
#             if jaja=="123":
#                 menu_empleado()
#             else:
#                 print("Contraseña incorrecta...")
#                 esperarTecla()
#         elif opcion=="3" or opcion=="SALIR":
#             print("¡¡Adios!!")
#             break
                

# def menu_clientes():
#     while True:
#         borrarPantalla()
#         print("""
#     .::Menu de Clientes::.
#             1.- Mostrar tus datos.
#             2.- Actualizar tus datos.
#             3.- Darte de baja de la aplicacion.
#             4.- Salir
#               """)
#         opcion= input("Selecciona una de las opciones anteriores").upper()
        
#         if opcion=='1' or opcion =="MOSTRAR":
#             borrarPantalla()
#             id_clientes=input("\t Coloca tu id proporcionado por el empleado: ")
#             #Agregar codigo  
#             registros=cliente.Cliente.mostrar(id_clientes)
#             if len(registros)>0:
#                 num_notas=1
#                 for fila in registros:
#                    print(f"\n Id: {fila[0]}   .- Nombre: {fila[1]}         Apellidos {fila[2]} \t Numero de plan: {fila[3]}  ") 
#                    num_notas+=1    
#             else:
#                 print(f"\n \t \t** No existen clientes  ... vuelva a intentarlo **...")
#             esperarTecla()
            
#         elif opcion=='2' or opcion=="ACTUALIZAR":
#             borrarPantalla()
#             id_clientes=input("\t Id del cliente a actualizar")
#             nombre= input("\t \t Nombre: ")
#             apellidos= input("\t Coloca tus apellidos: ")
#             plan= input("\t Coloca el plan a elegir")
#              #Agregar codigo
#             resultado=cliente.Cliente.actualizar(id_clientes,nombre, apellidos, plan)
#             if resultado:
#                 print(f"\n \t \t.::Cliente Actualizado Correctamente ::.")
#                 esperarTecla
#             else:
#                 print(f"\n \t \t** No fue posible actualizar al cliente ... vuelva a intentarlo **...")  
#             esperarTecla()
            
#         elif opcion=='3' or opcion=="ELIMINAR":
#             id_clientes= input("\t \t Id del cliente a eliminar: ")
#             #Agregar codigo
#             resultado=cliente.Cliente.eliminar(id_clientes)
#             if resultado:
#                 print("\t \t El cliente se elimino con exito.")
#             else:
#                 print("\t \t El Cliente no se pudo eliminar... Asegurate que el ID sea el correcto.")
#             esperarTecla()
#         elif opcion=='4' or opcion=="SALIR":
#             print("\t !!Gracias por usar nuestro software¡¡")
#             break
#         else:
#             print("Asegurate que la opcion sea la correcta")
#             esperarTecla()

# def menu_empleado():
    
#     while True:
#         borrarPantalla()
#         print("""
#     ..::Menu Empleados::..
#             1.-Modificar Planes
#             2.- Modificar Clientes
#             3.- Acceder Servicios
#             4.- Modificar Empleados
#             5.- Salir
            
#             """)
#         opcion=input("Selecciona una de las opciones anteriores para poder continuar: ").upper()
#         if opcion=="1" or opcion=="PLANES" or opcion=="MODIFICAR PLANES":
#             modificarPlanes()
#         elif opcion=="2" or opcion=="CLIENTES" or opcion=="MODIFICAR CLIENTES":
#             modificarClientes()
#         elif opcion=="3" or opcion=="SERVICIOS" or opcion=="ACCEDER SERVICIOS":
#             accederServicios()
#         elif opcion=="4" or opcion=="EMPLEADOS" or opcion=="MODIFICAR EMPLEADOS":
#             modificarEmpleados()
#         elif opcion=="5" or opcion=="SALIR":
#             break
#         else: 
#             print("Opcion incorrecta, vuelve a intentar...")
#             esperarTecla()

# def modificarPlanes():
    
#     while True:
#         borrarPantalla()
#         print ("")
#         print("""
#     ..::Menú de Planes::..
#               1.- Modificar precio...
#               2.- Modificar nombre...
#               3.- Añadir plan...
#               4.- Mostrar Planes
#               5.- Salir""")
#         opcion=input("Selecciona una de las opciones anteriores:")
#         if opcion=="1" or opcion=="PRECIO" or opcion=="MODIFICAR PRECIO":
#             borrarPantalla()
#             id_plan=input("Coloca el ID del plan a modificar:  ")
#             precio_plan=input("Coloca el nuevo precio a modificar:  ")
#             resultado=plan.Plan.actualizarPrecio(id_plan,precio_plan)
#             if resultado:
#                 print("Se actualizo el precio correctamente: ")
#                 esperarTecla()
#             else: 
#                 print("Hubo un error al ejecutar, vuelve a intentarlo")
#                 esperarTecla()

#         elif opcion=="2" or opcion=="NOMBRE" or opcion=="MODIFICAR NOMBRE":
#             borrarPantalla()
#             id_plan=input("Coloca el id del plan a modificar:  ")
#             nombre_plan=input("Coloca el nuevo nombre del plan:  ")
#             resultado=plan.Plan.actualizarNombre(id_plan,nombre_plan)
#             if resultado:
#                 print("Se actualizo el nombre correctamente")
#                 esperarTecla()
#             else:
#                 print("Algo salio mal, vuelve a intentarlo...")
#                 esperarTecla()
#         elif opcion=="3" or opcion=="AÑADIR" or opcion =="AÑADIR PLAN":
#             borrarPantalla()
#             nombre_plan=input("Coloca el nombre del nuevo plan:  ")
#             precio_plan=input("COloca el precio del neuvo plan:  ")
#             resultado=plan.Plan.crear(nombre_plan,precio_plan)
#             if resultado:
#                 print("Se creo el plan correctamente.")
#                 esperarTecla()
#             else:
#                 print("ocurrio un error, verifica los datos...")
#                 esperarTecla()
#         elif opcion=="4" or opcion=="PLANES" or opcion=="MOSTRAR PLANES":
#             borrarPantalla()
#             mostrar=plan.Plan.mostrar()
#             if len(mostrar)>0:
#                 num_notas=1
#                 for fila in mostrar:
#                    print(f"\n Id del plan: {fila[0]}   .- Nombre: {fila[1]}         Precio: {fila[2]}   ") 
#                    num_notas+=1    
#             else:
#                 print(f"\n \t \t** No existen clientes  ... vuelva a intentarlo **...")
#             esperarTecla()
#         elif opcion=="5" or opcion=="SALIR":
#             break
#         else:
#             print("Coloca la opcion correcta... Vuelve a intentarlo")
#             esperarTecla()

# def modificarClientes():
#     while True:
#         borrarPantalla()
#         print("Datos del cliente utilizando su ID o agregar un nuevo cliente")
#         print("""
#     Menu Datos Cliente:
#             1.- Modificar datos del cliente...
#             2.- Agregar un nuevo cliente...
#             3.- Salir...""")
#         opcion=input("Selecciona una de las opciones anteriores:  ")
#         if opcion=="1" or opcion=="MODIFICAR" or opcion=="MODIFICAR DATOS DEL CLIENTE":
#             borrarPantalla()
#             id_cliente=input("Coloca el id del cliente a modificar:  ")
#             nombre=input("Coloca el nombre correcto:  ")
#             apellidos=input("Coloca los apellidos correctos:  ").lower()
#             plan=input("Coloca el ID del plan a actualizar:  ")
#             resultado=cliente.Cliente.actualizar(id_cliente,nombre,apellidos,plan)
#             if resultado:
#                 print("Se actualizaron los datos correctamente...")
#                 esperarTecla
#             else:
#                 print("Algo salio mal... Verifica los daltos.")
#                 esperarTecla()
#         elif opcion=="2" or opcion=="AGREGAR" or opcion=="AGREGAR UN NUEVO CLIENTE":
#             borrarPantalla()
#             nombre=input("Coloca el nombre del empleado:  ").lower()
#             apellidos=input("Coloca los apellidos del cliente:  ").lower()
#             plan=input("COloca el ID del plan:  ")
#             resultado=cliente.Cliente(nombre,apellidos,plan)
#             if resultado:
#                 print("Se creo el cliente correctamente...")
#                 esperarTecla()
#             else:
#                 print("Algo salio mal, verifica los datos...")
#         elif opcion=="3" or opcion=="SALIR":
#             break
        



# def accederServicios():
#     while True:
#         borrarPantalla()
#         print("Solo mostrar servicios")
#         print("""
#     ..::Menu Servicios::..
#             1.- Agregar servicio...
#             2.- Mostrar servicios...
#             3.- Volver al inicio...
#             4.- Salir""")
#         opcion=input("Selecciona una de las opciones anteriores:  ").upper()
#         if opcion=="1" or opcion=="AGREGAR" or opcion=="AGREGAR SERVICIO":
#             borrarPantalla()
#             cliente=input("Coloca el id del cliente:  ")
#             empleado=input("Coloca tu ID de empleado:  ")
#             descripcion=input("Coloca la descripcion del servicio").lower()
#             resultado=servicio.Servicio.crear(cliente,empleado,descripcion)
#             if resultado:
#                 print("Se creo el servicio correctamente...")
#                 esperarTecla()
#             else:
#                 print("Ocurrio un error, verifica los datos...")
#                 esperarTecla()
#         elif opcion=="2" or opcion=="MOSTRAR" or opcion=="MOSTRAR SERVICIOS":
#             borrarPantalla()
#             registros=servicio.Servicio.mostrar()
#             if len(registros)>0:
#                 num_notas=1
#                 for fila in registros:
#                    print(f"\n Id del servicio: {fila[0]}   .- Id del cliente: {fila[1]}         Id del empleado {fila[2]} \t Fecha: {fila[3]} \t Descripcion: {fila[4]}  ") 
#                    num_notas+=1    
#             else:
#                 print(f"\n \t \t** No existen servicios  ... vuelva a intentarlo **...")
#             esperarTecla()
#         elif opcion=="3" or opcion=="INICIO" or opcion=="VOLVER AL INICIO":
#             menu_empleado()
#         elif opcion=="4" or opcion=="SALIR":
#             break
#         else:
#             print("Selecciona una de las opciones anteriores")
#             esperarTecla()




# def modificarEmpleados():
#     while True:
#         borrarPantalla()
#         print("""
#     ..::Empleados::..
#             1.-Acceder a mis datos
#             2.-Agregar empleado
#             3.-volver al inincio
#             4.-Salir
#             """)
#         opc=input("Selecciona una de las opciones anteriores...  ").upper()
#         if opc=="1" or opc=="ACCEDER" or opc=="ACCEDER A MIS DATOS":
#             borrarPantalla()
#             id_empleado=input("Coloca tu id de empleado:  ")
#             resultado=empleados.Empleado.mostrar(id_empleado)
            
#             if len(resultado)>0:
#                 num_notas=1
#                 for fila in resultado:
#                     print(f"\n Id del empleado: {fila[0]}   .- Nombre: {fila[1]}         Apellidos: {fila[2]} \t Puesto: {fila[3]} \t Salario: {fila[4]} \t Horario: {fila[5]}  ") 
#                     num_notas+=1    
#             else:
#                 print(f"\n \t \t** No existen servicios  ... vuelva a intentarlo **...")
#             esperarTecla() 

#         elif opc=="2" or opc=="AGREGAR" or opc=="AGREGAR EMPLEADO":
#             borrarPantalla()
#             nombre=input("Coloca el nombre del empleado:  ").lower()
#             apellidos=input("Coloca los apellidos del empleado:  "). lower()
#             puesto=input("Coloca el puesto (recepcionista/entrenador):  ").lower()
#             salario=input("Coloca el salario del empleado:  ")
#             horario=input("Coloca el horario del empleado (matutino/vespertino):  ")
#             resultado=empleados.Empleado.crear(nombre,apellidos,puesto, salario, horario)
#             if resultado:
#                 print("Se creo el empleado correctamente...")
#             else:
#                 print("Asegurate de colocar los datos correctos...")
#                 esperarTecla()
#         elif opc=="3" or opc=="INICIO" or opc=="VOLVER AL INICIO":
#             menu_empleado()
#         elif opc=="4" or opc=="SALIR":
#             break
#         else:
#             print("Selecciona una de las opciones anteriores...")
#             esperarTecla()
        
    

# if __name__ == "__main__":
#   menu_InicioSesion()