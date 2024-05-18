#edad<0
#edad>0
edad=-1
while edad<0:
    print("Ingresa tu edad")
    edad=int(input())   
    if edad<0:
        print("La edad no puede ser negativa")

print("Segundo while")
while not edad>0:
    print("ingresa tu edad")
    edad=int(input())
    if edad<0:
        print("La edad no puede ser negativa")