def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    **Conceptos:** `input()`, concatenación de strings (`+`), `lower()`, `title()`, `upper()`, caracter de escape (`\t`).

**Consigna:** Leer un nombre y un apellido mediante `input()`. Concatenarlos en un nombre completo y luego imprimir:

1. El nombre completo en minúsculas.
2. El nombre completo con formato título (primera letra de cada palabra en mayúscula).
3. El nombre completo en mayúsculas.
4. El nombre completo en minúsculas precedido por un tabulador.
    """
    nombre = str(input("Ingrese nombre: "))
    apellido = str(input("Ingrese apellido: "))
    nombre_completo = nombre + " " + apellido
    print(nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print("\t" + nombre_completo.lower())
    
#names()