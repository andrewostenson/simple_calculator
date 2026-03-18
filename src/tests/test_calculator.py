import pytest
from calculator.calculator import (
    circleArea,
    hypotenuse,
    percentage,
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
)

@pytest.mark.parametrize("n, expected", [
    (1, 3.14),
    (2, 12.56),
    (3, 28.26),
])
def test_circleArea(n, expected):
    assert circleArea(n) == expected

@pytest.mark.parametrize("n, m, expected", [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
])
def test_hypotenuse(n, m, expected):
    assert hypotenuse(n, m) == expected

@pytest.mark.parametrize("n, m, expected", [
    (1, 4, 25),
    (1, 2, 50),
    (3, 4, 75),
])
def test_percentage(n, m, expected):
    assert percentage(n ,m) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 4),
    (3, 9),
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (3, 6),
    (5, 15),
])
def test_triNums(n, expected):
    assert triNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (2, 4),
    (3, 7),
])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 15),
])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected
