def classificar_triangulo(a: int|float, b: int|float, c: int|float) -> str:
    if not all(isinstance(valor, (int, float)) for valor in (a,b,c)):
        raise TypeError("Lados devem ser valores numéricos")
    elif not all(valor > 0 for valor in (a,b,c)):
        raise ValueError("Lados devem ser positivos")
    elif not (
        a + b > c and
        a + c > b and
        c + b > a): ValueError("Lados não formam um triângulo")

    if a == b and b == c:
        return "Equilátero"
    elif (a == b and not b == c) or (b == c and not b == a):
        return "Isósceles"
    else:
        return "Escaleno"