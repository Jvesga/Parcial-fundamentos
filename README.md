# Parcial 1 Fundamentos de programacion 
## Ejercicio 1
Escriba un algoritmo que lea 2 números e imprima la suma de ellos si los dos números son pares o el producto si uno o ambos números son impar.
```py
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
```

## Ejercicio 2
Una tienda de electrónica está ofreciendo un descuento en los televisores. El descuento ofrecido se basa en el tamaño del televisor. 
Para un televisor de 14 pulgadas, se ofrece un 10% de descuento, mientras que, para televisores de 21 pulgadas, se está ofreciendo un descuento de 20%. 
Para los demás tamaños no se ofrece descuento.

Desarrollar el algoritmo para este problema.

```py
tamaño=int(input("Ingrese el tamaño del televisor en pulgadas: "))

#Descuentos

if (tamaño == 14):
    print("El descuento ofrecido para este tamaño de televisor es del 10%.")

elif (tamaño== 21):
    print("El descuento ofrecido para este tamaño de televisor es del 20%.")
    
else:
    print("Para este tamaño de televisor no se ofrece ningun tipo de descuento.")
```

## Ejercicio 3
¿Qué valor se almacena en las variables "y" (de tipo int) y "x" (de tipo float) al ejecutar cada una de estas sentencias?

### variables "y"

a) y = 2;
### Respuesta: 
En el caso de la variable "y" que es de tipo entero(int) el valor almacenado al ejecutar la sentencia (y=2) sera de "2" porque "2" es un entero y si es almacenable en "y".

b) y = 1 / 2;
### Respuesta: 
En este caso en el que la sentencia es (y=1/2) o (0,5), no es posible almacenar este valor en "y" ya que no es un entero y variable solo puede almacenar numeros sin decimales. 

### variables "x"

c) x = 2.0 / 4;
g) x = 2 / 4;

### Respuesta:
Al ejecutar estas dos sentencias en las que tenemos decimales si es posible Para "x" tomar valores no enteros ya que es una variable de tipo float 
por tanto puede almacenar valores decimales como los dados en el ejemplo (2.0/4)o(0.5) y (2/4)o(0.5) 
