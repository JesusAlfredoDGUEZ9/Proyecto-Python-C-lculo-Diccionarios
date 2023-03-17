#SISTEMA DE CANASTA BÁSICA.

print("Hola bienvenido estimado usuari@. \nEste el sistema de la canasta básica, podrás calcular cuanto pagarás en total por producto o por productos."
      " \n'MARKERTUXTEPEC'")

#Datos o Información.
Canasta_basica = {"Huevo. 60 piezas" : 80, "Aceite Nutrioli. 1 Litro" : 37, "Leche Lala Deslactosada" : 23, "Tomate Saladet" : 18.50, "Sopa. Moderna" : 7,
                  "Atun. El Dorado" : 18, "Frijol 1kg. El Bueno" : 25, "Arroz 1kg. El Bueno" : 25, "Sal 1kg" : 19.50, "Avena" : 21, "Pasta Dental" : 15,
                  "Chiles Envasados" : 22, "Lentejas" : 19, "Galletas Marias" : 15, "Pan" : 15}

#Datos
print("\n")
print("PRODUCTOS")
Producto =  Canasta_basica[input("Ingresa el producto que desea registrar: ")]
Producto2 =  Canasta_basica[input("Ingresa el segundo producto que desea registrar: ")]
Producto3 =  Canasta_basica[input("Ingresa el tercer producto que desea registrar: ")]
Producto4 =  Canasta_basica[input("Ingresa el cuarto producto que desea registrar: ")]
Producto5 =  Canasta_basica[input("Ingresa el quinto producto que desea registrar: ")]

print("\n")
print("CANTIDAD")
cantidad1 = int(input("Ingresa la cantidad/piezas del producto: "))
cantidad2 = int(input("Ingresa la cantidad/piezas del segundo producto: "))
cantidad3 = int(input("Ingresa la cantidad/piezas del tercer producto: "))
cantidad4 = int(input("Ingresa la cantidad/piezas del cuarto producto: "))
cantidad5 = int(input("Ingresa la cantidad/piezas del quinto producto: "))


calculo1 = Producto * cantidad1
calculo2 = Producto2 * cantidad2
calculo3 = Producto3 * cantidad3
calculo4 = Producto4 * cantidad4
calculo5 = Producto5 * cantidad5

totalpago = (calculo1 + calculo2 + calculo3 + calculo4 + calculo5)

print("\n")
print ("CARRITO")
print("\n")
print (f"Precio del producto: ${Producto}.00 \nPrecio del total del producto: ${calculo1}.00")
print("\n")
print (f"Precio del segundo producto: ${Producto2}.00 \nPrecio del total del producto: ${calculo2}.00")
print("\n")
print (f"Precio del tercer producto: ${Producto3}.00 \nPrecio del total del producto: ${calculo3}.00")
print("\n")
print (f"Precio del cuarto producto: ${Producto4}.00 \nPrecio del total del producto: ${calculo4}.00")
print("\n")
print (f"Precio del quinto producto: ${Producto5}.00 \nPrecio del total del producto: ${calculo5}.00")


print("\n")
print ("TOTAL")
print (f" TOTAL A PAGAR = ${totalpago}mx")





