print("Venta de franelas")
print("Talla   Precio")
print("S       50")
print("M       55")
print("L       60")
print("XL      65")
nombre=input("Ingresa tu nombre")
cant=int(input("Cuantos va a comprar"))
talla=input("Ingrese la talla").upper()

precio=0
match talla:
    case "S":
        precio=50
    case "M":
        precio=55
    case "L":
        precio=60
    case "XL":
        precio=65
    case "XXL":
        precio=70
    case _:
        print("Talla invalida")
talla_valida=(talla=="S" or talla=="M" or talla=="L" or talla=="XL" or talla=="XXL")

porc=0
if cant>6 and cant<12:
    porc=0.05
elif cant>12 and cant<24:
    porc=0.1
if cant>24:
    porc=0.15

subtotal=precio*cant
monto_descuento=subtotal*porc
monto_total=subtotal-monto_descuento


if cant>0:
    print(f"Talla seleccionada es {talla} y su precio {precio}")
if not talla_valida:
    print("No se puede procesar la venta")
    print("Ha ingresado datos invalidos")

print(f"{nombre}")
print(f"Usted llevara {cant} de franelas de la talla {talla}")
print(f"Su subtotal a pagar es {subtotal}$")
print(f"Su monto total a pagar es {monto_total}$")
