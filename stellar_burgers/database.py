from typing import List

from stellar_burgers.bun import Bun
from stellar_burgers.ingredient import Ingredient
from stellar_burgers.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Database:
    """
    Класс с методами по работе с базой данных.
    """

    def __init__(self):
        self.buns: List[Bun] = []
        self.ingredients: List[Ingredient] = []

        self.buns.append(Bun("black bun", 100))
        self.buns.append(Bun("white bun", 200))
        self.buns.append(Bun("red bun", 300))

        self.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300))

        self.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))

    # Возвращает список доступных булок
    def available_buns(self) -> List[Bun]:
        return self.buns

    #  Возвращает список доступных ингредиентов
    def available_ingredients(self) -> List[Ingredient]:
        return self.ingredients

    # Добавляет булку в базу данных. :param bun: Объект булки.
    def add_bun(self, bun: Bun):
        self.buns.append(bun)

    # Возвращает список всех булок в базе данных.
    def get_buns(self) -> List[Bun]:
        return self.buns

    # Добавляет ингредиент в базу данных.  :param ingredient: Объект ингредиента.
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    # Возвращает список всех ингредиентов в базе данных.
    def get_ingredients(self) -> List[Ingredient]:
        return self.ingredients