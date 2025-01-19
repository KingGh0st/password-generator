import random

while True:
    try:
        longitud = int(input("Introduzca longitud de contraseña: "))
        break
    except ValueError:
        print("Cucha poné un entero no sea boludo.")
    except TypeError:
        print("Cucha poné un entero no sea boludo.")

mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"
numeros = "123456789"
simbolos = "[](){}*,/.;_-:"

todo = mayusculas + minusculas + numeros + simbolos

password = "".join(random.sample(todo,longitud))
print(password)