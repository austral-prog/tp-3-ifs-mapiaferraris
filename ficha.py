def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """

    nombre_completo= input(f"Ingrese nombre completo: ").strip()
    email = input(f"Ingrese email: ")
    nota_1 = int(input(f"Ingrese su nota 1: "))
    nota_2 = int(input(f"Ingrese su nota 2: "))
    nota_3 = int(input(f"Ingrese su nota 3: "))
    encabezado = """========================
    FICHA DEL ALUMNO
========================"""

    print (encabezado)
    print (f"Nombre: {nombre_completo.title().strip()}")
    print (f"Email: {email.lower()}")
    print (f"Caracteres en nombre: {len(nombre_completo)}")
    space = nombre_completo.find(" ")
    iniciales = nombre_completo[0] + nombre_completo[space + 1]
    print (f"Iniciales: {iniciales.upper()}")
    print (f"Usuario: {nombre_completo[space + 1:].lower() + '.' + nombre_completo[0:space].lower()}")
    print (f"Email valido: {'@' in email}")
    arroba = email.find("@")
    dominio = email[(arroba+1):]
    print (f"Dominio: {dominio.lower()}")
    print (f"Nombre para archivo: {nombre_completo.replace(' ', '_').title()}")
    print(f"Cantidad de a: {nombre_completo.lower().count('a')}")
    print (f"Codigo secreto: {nombre_completo[::-1].upper()}")
    print (f"Nota 1: {nota_1}")
    print (f"Nota 2: {nota_2}")
    print (f"Nota 3: {nota_3}")
    print (f"Suma: {nota_1 + nota_2 + nota_3}")
    print (f"Promedio: {(nota_1 + nota_2 + nota_3)/3}")
    print (f"Promedio entero: {(nota_1 + nota_2 + nota_3)//3}")
    print (f"="*24)

#ficha()



