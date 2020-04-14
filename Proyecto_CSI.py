#Recursos a utilizar
numeros = []
sw = True
#Logica del programa
#Para la suma
def suma_de_numeros():
    numero1 = int(input('Ingrese un numero: '))
    numeros.append(numero1)
    numero2 = int(input('Ingrese otro numero: '))
    numeros.append(numero2)
    print('El resultado es: ', numero1 + numero2)
#Para la resta
def resta_de_numeros():
    numero1 = int(input('Ingrese un numero: '))
    numeros.append(numero1)
    numero2 = int(input('Ingrese otro numero: '))
    numeros.append(numero2)
    print('El resultado es: ', numero1 - numero2)
#Para la multiplicacion
def multiplicacion_de_numeros():
    numero1 = int(input('Ingrese un numero: '))
    numeros.append(numero1)
    numero2 = int(input('Ingrese otro numero: '))
    numeros.append(numero2)
    print('El resultado es: ', numero1 * numero2)
#Para la division
def division_de_numeros():
    numero1 = int(input('Ingrese un numero: '))
    numeros.append(numero1)
    numero2 = int(input('Ingrese otro numero: '))
    numeros.append(numero2)
    print('El resultado es: ', numero1 / numero2)
#Para opcion no disponible
def opcion_no_disponible():
    print('Opcion no disponible')
#Para terminar el programa
def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False

#Interfaz del programa
menu = '''
====CALCULADORA===
1. SUMA
2. RESTA
3. MULTIPLICACION
4. DIVISION
5. SALIR'''
while sw:
    print(menu)
    opcion = int(input('Ingrese una opcion: '))
    if opcion == 1:
        print('Suma de numeros')
        suma_de_numeros()
    elif opcion == 2:
        print('Resta de numeros')
        resta_de_numeros()
    elif opcion == 3:
        print('Multiplicacion de numeros')
        multiplicacion_de_numeros()
    elif opcion == 4:
        print('Division de numeros')
        division_de_numeros()
    elif opcion == 5:
        terminar_programa()
    else:
        opcion_no_disponible()