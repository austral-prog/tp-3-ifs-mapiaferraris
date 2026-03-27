def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = str(input("Ingrese nombre:"))

    check_a = ("a" in nombre.lower())
    check_e = ("e" in nombre.lower())
    check_i = ("i" in nombre.lower())
    check_o = ("o" in nombre.lower())
    check_u = ("u" in nombre.lower())

    print(f"Contiene a: {check_a}")
    print(f"Contiene e: {check_e}")
    print(f"Contiene i: {check_i}")
    print(f"Contiene o: {check_o}")
    print(f"Contiene u: {check_u}")

#check_vowels()
