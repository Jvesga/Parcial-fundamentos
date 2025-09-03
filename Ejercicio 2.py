#Una tienda de electrónica está ofreciendo un descuento en los televisores. 
# El descuento ofrecido se basa en el tamaño del televisor. 
# Para un televisor de 14 pulgadas, se ofrece un 10% de descuento, mientras que, para televisores de 21 pulgadas, se está ofreciendo un descuento de 20%. 
# Para los demás tamaños no se ofrece descuento.

#Desarrollar el algoritmo para este problema.

tamaño=int(input("Ingrese el tamaño del televisor en pulgadas: "))

#Descuentos

if (tamaño == 14):
    print("El descuento ofrecido para este tamaño de televisor es del 10%.")

elif (tamaño== 21):
    print("El descuento ofrecido para este tamaño de televisor es del 20%.")
    
else:
    print("Para este tamaño de televisor no se ofrece ningun tipo de descuento.")