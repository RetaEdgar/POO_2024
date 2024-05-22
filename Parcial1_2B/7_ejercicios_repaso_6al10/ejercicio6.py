#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

numero=int(input("Ingrese un numero: "))

multi=0
i=1
while i<=10:
    multi=numero*i
    print(f"{numero} X {i} = {multi}")
    i+=1
