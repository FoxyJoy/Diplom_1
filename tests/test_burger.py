import pytest
from stellar_burgers.burger import Burger
from stellar_burgers.bun import Bun
from stellar_burgers.ingredient import Ingredient

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun("blue bun", 100)

@pytest.fixture
def ingredient():
    return Ingredient("sauce", "Spice-X", 50)

def test_set_buns(burger, bun):
    burger.set_buns(bun)
    assert burger.get_price() == 200

def test_add_ingredient(burger, bun, ingredient):
    burger.set_buns(bun)  # Устанавливаем булку
    burger.add_ingredient(ingredient) # Добавляем ингредиент
    assert burger.get_price() == 250 # Цена булки * 2 + цена ингредиента

def test_get_receipt(burger,bun, ingredient):
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    # assert "Bun: blue bun" in receipt
    # assert "sauce: Spice-X" in receipt
    # assert "Price: 250" in receipt
    assert "(==== blue bun ====)" in receipt
    assert "= sauce Spice-X =" in receipt
    assert "Price: 250" in receipt
