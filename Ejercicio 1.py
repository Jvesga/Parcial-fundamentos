#Escriba un algoritmo que lea 2 números e imprima la suma de ellos si los dos números son pares o el producto si uno o ambos números son impar.

print("Por favor solo dijite numeros enteros")
numero1=int(input("Dijite el primero numero: "))
numero2=int(input("Dijite el segundo numero: "))

if (numero1 % 2 != 0) or (numero2 % 2 != 0):
    producto=(numero1 * numero2) 
    print("uno de los numeros ingresados es impar")
    print("El producto de los numeros ingresados es: " , producto)
else:
    sumar = numero1 + numero2
    print("Los numeros ingresados son pares")
    print("La suma de los numero ingresados es de: ", sumar)