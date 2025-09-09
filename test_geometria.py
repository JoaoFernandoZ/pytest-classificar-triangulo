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

# --- [ Testes de Tratamento de Erros (Error Handling) ] --- #

@pytest.mark.error_handling
@pytest.mark.parametrize(
    "a, b, c",
    [
        # Caso 1: Lado A Negativo
        (-5, 5, 5),

        # Caso 2: Lado B Negativo
        (5, -5, 4),

        # Caso 3: Lado C Negativo
        (11, 4, -8),
    ],
    ids = ["lado_a_negativo", "lado_b_negativo", "lado_c_negativo"]
)
def test_classificar_triangulo_lados_negativos(a, b, c):
    with pytest.raises(ValueError, match="Lados devem ser positivos"):
        classificar_triangulo(a, b, c)

@pytest.mark.error_handling
@pytest.mark.parametrize(
    "a, b, c",
    [
        # Caso 1: Lado A do tipo String
        ("cinco", 5, 5),

        # Caso 2: Lado B do tipo lista
        (5, [5], 4),

        # Caso 3: Lado C do tipo lista com String
        (11, 4, ["oito"]),
    ],
    ids = ["lado_a_negativo", "lado_b_negativo", "lado_c_negativo"]
)
def test_classificar_triangulo_tipos_invalidos(a, b, c):
    with pytest.raises(TypeError, match="Lados devem ser valores numéricos"):
        classificar_triangulo(a, b, c)