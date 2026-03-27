def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    
    precio = int(input("Ingrese precio: "))
    descuento = float(input("Ingrese descuento: "))
    cantidad = int(input("Ingrese cantidad: "))

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")

    precio_con_descuento = precio - descuento 
    precio_total = precio_con_descuento * cantidad

    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {precio_total}")

#casting()