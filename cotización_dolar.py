#Crear desde la línea de comandos un sistema donde podrás ingresar el monto que deseas cambiar

def usdPyg():
    cant = int(input("Ingrese cantidad de dolar: "))
    res = cant * 6514
    print(res)
    return
def pygUsd():
    cant = int(input("Ingrese cantidad de guaranies: "))
    res = cant / 6514
    print(res)
    return

print("Bienvenido al programa de cotización del dólar")
print("1) USD a PYG")
print("2) PYG a USD")
op = int(input("Ingrese opcion: "))

if (op == 1):
    usdPyg()
elif(op == 2):
    pygUsd()
else:
    print("Error 404.")
