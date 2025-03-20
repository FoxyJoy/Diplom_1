import pytest
from stellar_burgers.bun import Bun
from stellar_burgers.database import Database
from stellar_burgers.ingredient import Ingredient

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def bun():
    return Bun("black bun", 100)

@pytest.fixture
def ingredient():
    return Ingredient("sauce", "hot sauce", 50)

# Добавляет булку в базу данных
def test_add_bun(database, bun):
    # 1. Добавляем булку в базу данных
    database.add_bun(bun)
    # 2. Проверяем, что количество булок увеличилось на 1
    assert len(database.get_buns()) == 4  # 3 булки уже есть в базе, добавляем ещё одну
    # 3. Проверяем, что первая булка в списке имеет правильное имя
    assert database.get_buns()[0].get_name() == "black bun"
    # 4. Проверяем, что добавленная булка находится в списке
    assert bun in database.get_buns()

# Добавляет ингредиенты в базу данных
def test_add_ingredient(database, ingredient):
    # 1. Добавляем ингредиент в базу данных
    database.add_ingredient(ingredient)
    # 2. Проверяем, что количество ингредиентов увеличилось на 1
    assert len(database.get_ingredients()) == 7  # 6 ингредиентов уже есть в базе, добавляем ещё один
    # 3. Проверяем, что последний добавленный ингредиент имеет правильное имя
    assert database.get_ingredients()[6].get_name() == "hot sauce"