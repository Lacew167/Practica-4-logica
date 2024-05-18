nombre=input("Como te llamas?")
edad=int(input("Cuantos anos tienes?"))
estado_civil=input("Ingresta tu estado civil (S)oltero (C)asado (P)areja ").upper()
#variables logicas
mayor_edad=(edad>17)
soltera=(estado_civil=="S")
pareja=(estado_civil=="P")
casado=(estado_civil=="C")

if mayor_edad:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es Menor de edad")

if not mayor_edad: #evaluamos si no se cumpla la condicicon edad>17
    print(f"{nombre} es Menor de edad")
else:
    print(f"{nombre} es Mayor de edad")

if not soltera:
    print(f"{nombre} no esta soltera")
else:
    print(f"{nombre} esta soltero")

if not pareja:
    print(f"{nombre} no tiene pareja")
else:
    print(f"{nombre} tiene pareja")

if not casado:
    print(f"{nombre} no esta casado")
else:
    print(f"{nombre} esta casado")
