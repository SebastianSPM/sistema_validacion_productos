print("\n****************************************************")
print("***BIENVENID@S SISTEMA DE VALIDACION DE PRODUCTOS***")
print("****************************************************\n")

# Entrada de datos
bandera = 1

while bandera != 0:
    while bandera != 0:
        try:
            nombreProducto = input("\nIngrese el nombre del producto: ")
            nombreProducto = nombreProducto.split()
            nombreProducto = " ".join(nombreProducto)

            if len(nombreProducto) == 0:
                print("\nNo colocaste ningun nombre")
            else:
                bandera = 0
        except ValueError:
            print("\nPor favor ingrese un nombre válido")

    #Pidiendo al usuario precio unitario
    bandera = 1

    while bandera != 0:
        try:
            precioUnitario = float(input("\nIngrese el precio unitario del producto: "))
            if precioUnitario <= 0:
                print("\nEl precio debe ser mayor a cero.")
            else:
                bandera = 0
        except ValueError:
            print("\nPor favor ingrese un valor numérico válido para el precio.")

    #Pidiendo al usuario cantidad de productos adquiridos
    bandera = 1

    while bandera != 0:
        try:
            cantidad = int(input("\nIngrese la cantidad de productos adquiridos: "))
            if cantidad <= 0:
                print("\nLa cantidad debe ser mayor a cero.")
            else:
                bandera = 0
        except ValueError:
            print("\nPor favor ingrese un valor entero válido para la cantidad.")

    #Pidiendo al usuario porcentaje de descuento
    bandera = 1

    while bandera != 0:
        try:
            descuento = float(input("\nIngrese el porcentaje de descuento (si no hay descuento ingrese 0): "))
            if descuento < 0:
                print("\nEl descuento no puede ser negativo.")
            else:
                if descuento > 100:
                    print("El descuento es superado, intente de nuevo\n")
                else:
                    bandera = 0
        except ValueError:
            print("\nPor favor ingrese un valor numérico válido para el descuento.")

    # Proceso
    #Calculando
    iva = 0.19
    sinDescuento = precioUnitario * cantidad
    montoDescuento = sinDescuento * (descuento / 100)
    ivaAplicado = (sinDescuento - montoDescuento) * iva
    totalPagar = (sinDescuento - montoDescuento) + ivaAplicado

    # Mostrar resumen de la compra
    #Salida de datos
    print("\n===========================================")
    print(f"Resumen de la compra:")
    print(f"Producto: {nombreProducto}")
    print(f"Costo sin descuento: ${sinDescuento:.2f}")
    print(f"Descuento aplicado: -${montoDescuento:.2f}")
    print(f"Subtotal con descuento: ${(sinDescuento - montoDescuento)}")
    print(f"IVA (19%) ${ivaAplicado}")
    print(f"Costo total a pagar: ${totalPagar:.2f}")
    print("===========================================\n")

    bandera = input("Quieres ingresar más productos?(S/N)")
    if bandera.lower() == "s":
        bandera = 0
        
