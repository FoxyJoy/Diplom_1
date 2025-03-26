import pytest
from stellar_burgers.burger import Burger
from stellar_burgers.bun import Bun
from stellar_burgers.ingredient import Ingredient
from stellar_burgers.ingredient_types import *
from unittest.mock import Mock

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

def test_get_receipt():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "blue bun"
    mock_bun.get_price.return_value = 120
    mock_ing_sauce = Mock()
    mock_ing_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ing_sauce.get_name.return_value = "spicy sauce"
    mock_ing_sauce.get_price.return_value = 90
    mock_ing_filling = Mock()
    mock_ing_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ing_filling.get_name.return_value = "bacon"
    mock_ing_filling.get_price.return_value = 150
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ing_sauce)
    burger.add_ingredient(mock_ing_filling)
    assert burger.get_receipt() == ('(==== blue bun ====)\n'
                                    '= sauce spicy sauce =\n'
                                    '= filling bacon =\n'
                                    '(==== blue bun ====)\n'
                                    '\n'
                                    'Price: 480')

def test_remove_ingredient():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "blue bun"
    mock_bun.get_price.return_value = 120
    mock_ing_sauce = Mock()
    mock_ing_sauce.get_name.return_value = "spicy sauce"
    mock_ing_sauce.get_price.return_value = 90
    mock_ing_filling = Mock()
    mock_ing_filling.get_name.return_value = "bacon"
    mock_ing_filling.get_price.return_value = 150
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ing_sauce)
    burger.add_ingredient(mock_ing_filling)
    burger.remove_ingredient(0)
    assert mock_ing_sauce not in burger.ingredients

def test_move_ingredient():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "blue bun"
    mock_bun.get_price.return_value = 120
    mock_ing_filling = Mock()
    mock_ing_filling.get_name.return_value = "bacon"
    mock_ing_filling.get_price.return_value = 150
    mock_ing_sauce_first = Mock()
    mock_ing_sauce_first.get_name.return_value = "spicy sauce"
    mock_ing_sauce_first.get_price.return_value = 90
    mock_ing_sauce_second = Mock()
    mock_ing_sauce_second.get_name.return_value = "mustard"
    mock_ing_sauce_second.get_price.return_value = 60
    burger.set_buns(mock_bun)
    # Добавляем два ингредиента
    burger.add_ingredient(mock_ing_filling)
    burger.add_ingredient(mock_ing_sauce_first)
    burger.add_ingredient(mock_ing_sauce_second)
    # Перемещаем ингредиенты
    burger.move_ingredient(2, 0)
    assert burger.ingredients[0] == mock_ing_sauce_second

