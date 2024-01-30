import funcionesmath as fmath
import menu as menu
import proyecto as proyecto
from datetime import date




today = date.today()
print(today)
print("<<<Autor: Jose Maximiliano Mora Sepulveda>>>")


#aqui estaba mi menu


menu.menu()




selecion = int(input())




num1 = int(input("Ingrese el primer numero a operar:"))
num2 = int(input("Ingrese el segundo numero a operar:"))
m = "m"
M = "M"




if selecion == 1:
     print("La Suma de tus numeros es:", fmath.suma(num1, num2))
elif selecion == 2:
    print("La Resta de tus numerons es :", fmath.resta(num1, num2))
elif selecion == 3:
     print("La Raiz Cuadrada es: ", fmath.sqrt(num1))
elif selecion == 4:
     print("La Multiplicasion es:", fmath.multiplicasion(num1, num2))
elif selecion == 5:
     print("La Divicion es:", fmath.division(num1, num2))
elif selecion == m or selecion == M:
      menu()
