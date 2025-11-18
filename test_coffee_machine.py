import pytest
from coffee_machine import CoffeeMachine

def test_make_small_coffee_success():
    machine = CoffeeMachine()
    result = machine.make_coffee(size="pequeño", sugar=2)
    assert result == "Recoge tu café pequeño ☕ con 2 cucharadas de azúcar."

def test_make_medium_coffee_success():
    machine = CoffeeMachine()
    result = machine.make_coffee(size="mediano", sugar=1)
    assert result == "Recoge tu café mediano ☕ con 1 cucharada de azúcar."

def test_make_large_coffee_success():
    machine = CoffeeMachine()
    result = machine.make_coffee(size="grande", sugar=3)
    assert result == "Recoge tu café grande ☕ con 3 cucharadas de azúcar."

def test_invalid_size():
    machine = CoffeeMachine()
    with pytest.raises(ValueError, match="Tamaño de vaso no válido"):
        machine.make_coffee(size="gigante", sugar=2)

def test_no_cups_left():
    machine = CoffeeMachine()
    machine.cups = {"pequeño": 0, "mediano": 0, "grande": 0}
    with pytest.raises(ValueError, match="No hay vasos disponibles"):
        machine.make_coffee(size="pequeño", sugar=1)

def test_no_coffee_left():
    machine = CoffeeMachine()
    machine.coffee_amount = 0
    with pytest.raises(ValueError, match="No hay café disponible"):
        machine.make_coffee(size="mediano", sugar=1)

def test_no_sugar_left():
    machine = CoffeeMachine()
    machine.sugar_amount = 0
    with pytest.raises(ValueError, match="No hay azúcar disponible"):
        machine.make_coffee(size="pequeño", sugar=1)
