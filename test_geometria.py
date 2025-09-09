import pytest
from geometria import classificar_triangulo



# --- [ Testes de Caminho Feliz (Happy Path) ] --- #

@pytest.mark.happy_path
@pytest.mark.parametrize(
    "a, b, c, categoria_esperada",
    [
        # Caso 1: Triângulo Equilátero
        (5, 5, 5,       "Equilátero"),

        # Caso 2: Triângulo Isósceles
        (5, 5, 4,       "Isósceles"),

        # Caso 3: Triângulo Escaleno
        (11, 4, 8,      "Escaleno"),
    ],
    ids = ["equilátero", "isósceles", "escaleno"]
)
def test_classificar_triangulo_cenarios_validos(a, b, c, categoria_esperada):
    resultado = classificar_triangulo(a, b, c)

    assert resultado == categoria_esperada
