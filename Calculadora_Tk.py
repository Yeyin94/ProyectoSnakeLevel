#Importando Tk
import tkinter as tk
#Declarando las variables a utilizar
numeros = []
root = tk.Tk()
mensaje= tk.StringVar()
numero1=tk.StringVar()
numero2=tk.StringVar()
resultado=tk.StringVar()
sw = False
#Logica del programa
#Para la suma
def suma_de_numeros():
    numeroA = int(numero1.get())
    numeros.append(numeroA)
    numeroB = int(numero2.get())
    numeros.append(numeroB)
    resultado.set(numeroA + numeroB)
    numero1.set('')
    numero2.set('')
def resta_de_numeros():
    numeroA = int(numero1.get())
    numeros.append(numeroA)
    numeroB = int(numero2.get())
    numeros.append(numeroB)
    resultado.set(numeroA - numeroB)
    numero1.set('')
    numero2.set('')
def multiplicacion_de_numeros():
    numeroA = int(numero1.get())
    numeros.append(numeroA)
    numeroB = int(numero2.get())
    numeros.append(numeroB)
    resultado.set(numeroA * numeroB)
    numero1.set('')
    numero2.set('')
def division_de_numeros():
    numeroA = int(numero1.get())
    numeros.append(numeroA)
    numeroB = int(numero2.get())
    numeros.append(numeroB)
    resultado.set(numeroA / numeroB)
    numero1.set('')
    numero2.set('')
root.geometry('300x300')
root.title('Calculadora')
root.config(bg='#7B1FA2')
tk.Label(root, text= 'CALCULADORA', bg='#7B1FA2', fg='white', font=('',20)).place(x=55,y=10)
#Para el numero 1
tk.Label(root, text= 'Primer numero', bg='#7B1FA2', fg='white', font=('',13)).place(x=16,y=70)
tk.Entry(root, justify='center', textvariable=(numero1)).place(x=152,y=75)
#Para el numero 2
tk.Label(root, text= 'Segundo numero', bg='#7B1FA2', fg='white', font=('',13)).place(x=16,y=110)
tk.Entry(root, justify='center', textvariable=(numero2)).place(x=152,y=115)
#Para el resultado
tk.Label(root, text= 'El resultado es: ', bg='#7B1FA2', fg='white', font=('',15)).place(x=20,y=200)
tk.Label(root, textvariable=resultado, bg='#7B1FA2', fg='white', font=('',15)).place(x=20,y=230)
#Boton para suma
tk.Button(root, text='SUMAR', bd=0, command=suma_de_numeros).place(x=20,y=160)
#Boton para resta
tk.Button(root, text='RESTAR', bd=0, command=resta_de_numeros).place(x=80,y=160)
#Boton para multiplicacion
tk.Button(root, text='MULTIPLICAR', bd=0, command=multiplicacion_de_numeros).place(x=140,y=160)
#Boton para division
tk.Button(root, text='DIVIDIR', bd=0, command=division_de_numeros).place(x=230,y=160)
#Boton para salir
tk.Label(root, textvariable=mensaje, bg='#7B1FA2', fg='white',font=('',20)).place(x=135,y=320)
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=135,y=270)
root.mainloop()