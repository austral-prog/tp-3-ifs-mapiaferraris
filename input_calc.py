def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Ingrese base: "))
    altura = int(input("Ingrese altura: "))

    area = base * altura
    perimetro = (2*base) + (2*altura)

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
#rectangle()