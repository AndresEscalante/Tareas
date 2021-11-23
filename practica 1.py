
print(">>----------Ejercicio 1----------<<")
print("Bienvenido usuario \nIntroduce un número entero ")

dato=int(input("> "))

for u in range(dato+1):
    print(" *"*u)





print("\n")
print(">>----------Ejercicio 2----------<<")
print("Bienvenido usuario \nIntroduce un número \nEntero positivo")

t=0
num=int(input("> "))

#for s in range(1,num+1):
    # print(" ", num-s,",")
#else:
   # print("Los números negativos no son permitidos")

if int:
    for s in range(num,-1,-1):
        print(s,end=",")
else:
    print("los negativos son falso")




print("\n")
print(">>----------Ejercicio 3----------<<")
print("Bienvenido usuario \nIntroduce un número entero ")

nom =int(input("> "))

for n in range(2, nom):
   if nom % n == 0:

            print(nom, "No es primo")

print(nom, "es primo")