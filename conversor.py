def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #redondeamos dolares a 2 decimales
    dolares = str(dolares)
    print("Tienes $"+ dolares + "dolares")

menu = """
Bienvenido al conversor de monedas💱🪙

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos mexianos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor("colombianos", 3875)
elif opcion == '2':
    conversor("argentinos", 65)
elif opcion == '3':
    conversor("mexicanos", 24)
else:
    print(opcion +',no es una opción del menú, ''Por favor ingrese una opción correcta')

