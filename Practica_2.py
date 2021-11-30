#Grupo A : (mujeres con nombre anterior a la M y hombres con nombre posterior a la N)


print(">---------- Ejercicio 1 ----------<")
print("Bienvenido usuario \nIntrodusca los datos solicitados: ")

print("\n")

Name=input("Nombre > ")
SE= input("Sexo (Hombre o Mujer)> ") 



if SE=="Mujer":
    if Name<"M":
       group ="A"
    else:
        group ="B"

if SE=="Hombre":
    if Name>"N":
       group ="A"
    else:
        group ="B"



print("\n")
print("Nombre :" ,Name ,",", "Sexo :",SE ,",", "Grupo :",group )



print("\n")
print(">---------- Ejercicio 2 ----------<")
print("Bienvenido usuario  ")

class Producto():
 def __init__(self, codigo, nombre, precio, ContNeto):
    self.codigo= codigo
    self.nombre= nombre
    self.precio= precio
    self.ContNeto= ContNeto

pro = Producto(12, "Choco Titas Yogurt", 2, "10g")
 
print(pro.nombre, "Dulce sabor Chocolate con cobertura sabor yogurt")


Ut=int(input("Unidades a calcular : "))
costo = int(2)
calcular_tota= Ut * costo

print(calcular_tota)




