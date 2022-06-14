
'''
santi1 = 10
print (santi1)


saludo = "hola"
print (saludo)

rocio_perez = 225
print(rocio_perez)

x = 5
print(type(x))

y = "margarita"
print(type(y))

z = 5.4
print(type(z))



n1 = 10
n2 = 20

print(n1 * n2)

v1 = int(print("Ingrese el primer valor: "))
v2 = int(print("Ingrese el segundo valor: "))

resultado = v1 + v2

print("Esta es la suma de sus valores: ", resultado)

r=5
r *= 10
print(r)''' 


'''numero= float(input("Ingrese un numero, por favor:"))
if(numero == 0):
    print('El numero ingresado es 0')
elif(numero == 1):
    print('El numero ingresado es 1')
elif(numero <= 10):
    print('El numero ingresado es igual o mayor a 10')
else:
    print('El numero ingresa es mayor a 10')'''


nombre = str(input("\n Ingrese su nombre: ")) 
num1= int(input("\nIngrese el primer número: "))
num2= int(input("\nIngrese el segundo número: "))
num3= int(input("\n Ingrese el tercero número: "))

if (num1 > num2 and num1 > num3):
    print("\El mayor es el número 1: ", "***", num1,"***")
elif(num2 > num3 and num2 > num1):
    print("El número mayor es el 2")
elif(num3 > num1 and num3 > num2):
    print("El número mayor es el 3")
print("Muchas gracias",nombre)