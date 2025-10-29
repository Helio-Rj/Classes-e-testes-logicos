"""Módulo simples de calculadora com comentários educativos.

Este arquivo fornece a classe `Calculator` com operações aritméticas
básicas e um conjunto de testes unitários usando `unittest`.

Objetivo deste arquivo: servir como exemplo didático para aprender
sobre tipagem, tratamento de erros, docstrings e testes em Python.

Pontos importantes mostrados aqui:
- tipagem com `typing.Union` para aceitar `int` e `float`;
- validação de argumentos e lançamento de exceções apropriadas;
- uso de `unittest` para testar comportamentos esperados e erros.
"""

from typing import Union
import unittest

# Define o tipo "Number" como int ou float — facilita leitura e ferramentas
# de análise estática (hinting) como mypy ou editores com intellisense.
Number = Union[int, float]


class Calculator:
    """Calculadora básica com operações aritméticas.

    Cada método valida os tipos de entrada (aceita `int` e `float`) e
    retorna um número. As operações não tentam converter “strings” ou
    outros tipos implicitamente — preferimos falhar cedo com `TypeError`.
    """

    def _validate_numbers(self, a: Number, b: Number) -> None:
        """Valida se os parâmetros são números (int ou float).

        Lança `TypeError` se algum argumento não for um número. Separar
        essa validação em um método evita repetição e facilita testes.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os valores devem ser números (int ou float).")

    def add(self, a: Number, b: Number) -> Number:
        """Retorna a soma de `a` e `b`.

        Exemplo de uso: `calc.add(2, 3) -> 5`.
        """
        self._validate_numbers(a, b)
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """Retorna a subtração de `a` por `b` (a - b)."""
        self._validate_numbers(a, b)
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """Retorna o produto de `a` e `b` (a * b)."""
        self._validate_numbers(a, b)
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        """Retorna a divisão de `a` por `b`.

        Levanta `ValueError` quando `b == 0` para evitar divisão por zero.
        Note que a divisão retorna um `float` mesmo para inteiros quando
        necessário (comportamento do operador `/`).
        """
        self._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    def power(self, a: Number, b: Number) -> Number:
        """Retorna `a` elevado à potência `b` (a ** b)."""
        self._validate_numbers(a, b)
        return a ** b


# ---------------------------------------------------------------
# Bloco de testes automáticos
# Aqui testamos comportamento correto (valores esperados) e casos de
# erro (divisão por zero, tipo inválido). Esses testes servem como
# documentação executável do comportamento da classe.
# ---------------------------------------------------------------
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(9, 3), 3.0)

    def test_divide_by_zero(self):
        # espera-se ValueError ao tentar dividir por zero
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_invalid_type(self):
        # passar uma string deve causar TypeError (validação de tipos)
        with self.assertRaises(TypeError):
            self.calc.add("a", 2)


# ---------------------------------------------------------------
# Execução direta: demonstração e testes
# ---------------------------------------------------------------
if __name__ == "__main__":
    calc = Calculator()
    print("Demonstração manual:")
    # chamadas de demonstração: invocam métodos com números inteiros
    # e mostram os resultados no console.
    print("3 + 4 =", calc.add(3, 4))
    print("10 - 2 =", calc.subtract(10, 2))
    print("5 × 6 =", calc.multiply(5, 6))
    print("9 ÷ 3 =", calc.divide(9, 3))
    print("2 ^ 4 =", calc.power(2, 4))

    # Executa o runner do unittest. `argv=['']` evita que o
    # unittest.parse_args leia argumentos passados pela linha de comando
    # do ambiente (útil quando rodando em notebooks ou ambientes IDE).
    print("\nExecutando testes automáticos...\n")
    unittest.main(argv=[""], exit=False)
