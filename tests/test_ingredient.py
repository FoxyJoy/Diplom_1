import pytest
from stellar_burgers.ingredient import Ingredient
from stellar_burgers.ingredient_types import INGREDIENT_TYPE_SAUCE

# Проверяем, что ингредиенты представляют строку
def test_ingredient_str():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert str(ingredient) == "SAUCE: hot sauce ($100)"

# Проверяем, что при создании ингредиента с некорректными данными выбрасывается исключение
@pytest.mark.parametrize("ingredient_type, name, price, expected_exception", [
    ("", "hot sauce", 100, ValueError),  # Пустой тип
    ("filling", "", 200, ValueError),    # Пустое название
    ("filling", "beef", -5, ValueError), # Отрицательная цена
])
def test_invalid_ingredient_creation(ingredient_type, name, price, expected_exception):
        with pytest.raises(expected_exception):
            Ingredient(ingredient_type, name, price)

# Проверяем, что ингредиенты создаются
@pytest.mark.parametrize("ingredient_type, name, price", [
    ("sauce", "hot sauce", 100),
    ("filling", "cheese", 200),
    ("filling", "beef", 300),
])
def test_ingredient_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("sauce", "hot sauce", 100),
    ("filling", "cheese", 200),
    ("filling", "beef", 300),
])
def test_ingredient_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("sauce", "hot sauce", 100),
    ("filling", "cheese", 200),
    ("filling", "beef", 300),
])
def test_ingredient_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price
