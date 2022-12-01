from src import math_func
import pytest


@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9


@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10


@pytest.mark.number
def test_resta():
    assert math_func.resta(10, 15) == -5
    assert math_func.resta(2) == 0


@pytest.mark.strings
def test_add_strings():
    resultado = math_func.add('Hola', ' mundo')
    assert resultado == 'Hola mundo'
    assert type(resultado) is str
    assert 'Hola' in resultado
