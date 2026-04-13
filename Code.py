# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

#-----------------------------------------------
#Programa que dice si eres mayor de edad o no
x = int(input("Ingrese su edad\n"))

if x >= 18: 
    print("Felicidades! Eres mayor de edad!")
else: print("Aun eres menor de edad")

#-----------------------------------------------
#2


user1 = "pedro"
passwd1 = "1234"
user2 = "angel"
passwd2 = "1234"
u = input("Ingrese nombre de Usuario\n")
passwd = input("Ingrese contraseña\n")
if u == user1 and passwd == passwd1 or u == user2 and passwd == passwd2 or u:
    print(f"Bienvenido {u}, Puede usar el sistema")
    contador = 1 
else: print ("Datos Incorrectos intente de nuevo")

#----------------------------------------------
#3
# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.



nota1 = float(input("Ingrese Nota N1\n")) 
nota2 = float(input("Ingrese Nota N2\n")) 
nota3 = float(input("Ingrese Nota N3\n")) 


sum_notas = nota1 + nota2 + nota3 
prom_notas = sum_notas / 3

print(f"Tu promedio es: {prom_notas}\n")
if prom_notas >= 4.0:
    print("aprobado")
else: 
    print("Reprobado")

































