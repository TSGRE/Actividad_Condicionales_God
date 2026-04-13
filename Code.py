# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

#-----------------------------------------------
#1 Programa que dira si eres mayor de edad o no
x = int(input("Ingrese su edad\n"))
if x >= 18: 
    print("Felicidades! Eres mayor de edad!")
else: print("Aun eres menor de edad")
#-----------------------------------------------
#2 Programa que validara un usuario en el sistema

##Ingreso variables, usuarios y contraseñas que estaran guardadas en el sistema
user1 = "pedro"
passwd1 = 1234
user2 = "angel"
passwd2 = 1234
user3 = "tony"
passwd3 = 2623
## Incluimos un contador en falso para crear un acceso al usuario solo si cumple con el inicio de sesion
acceso = False

## Se agrega un while para que siempre vuelva a reintentar el usuario poder iniciar sesion
## Cuando el acceso sea 0 el usuario podra volver a iniciar sesion
while acceso == False:
    u = input("\n---Ingrese nombre de Usuario\n")
    ## El if validara si el usuario ingresado es correcto o no
    if u == user1 or u == user2 or u == user3:
        ## Se inserta un "try" para hacer que el usuario si o si entrege valores numericos en la contraseña
        try :
            passwd = int(input("---Ingrese Contraseña\n"))
            ## Si la contraseña ingresada por el usuario es correcta el programa le dara el acceso
            if (passwd == passwd1) or (passwd == passwd2) or (passwd == passwd3):
                print(f"---Bienvenido {u}, Puede usar el sistema!")
                acceso = 1
        ##  ## En caso no sea correcto el sistema se lo hara saber con comentarios        
            else: 
                print ("\n ***Contraseña Incorrecta Volviendo a iniciar sesion***\n")
        except: print("\n***Porfavor Solo valores validos, Intente Nuevamente***\n ") 
    else:
        print("\n***Usuario no encontrado, intente nuevamente***\n")


#----------------------------------------------
#3 Programa que aprueba o reprueba segun promedio


## Pedimos las 3 notas, y las guardamos en variables
nota1 = float(input("Ingrese Nota N1\n")) 
nota2 = float(input("Ingrese Nota N2\n")) 
nota3 = float(input("Ingrese Nota N3\n")) 

## Hacemos los calculos para crear el promedio
sum_notas = nota1 + nota2 + nota3 
prom_notas = sum_notas / 3


## Finalmente informamos al usuario si aprobo o no
print(f"\nTu promedio es: {prom_notas}\n")
if prom_notas >= 4.0:
    print("Aprobado!")
else:   
    print("Reprobado...")

































