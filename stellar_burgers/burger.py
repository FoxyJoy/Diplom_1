from typing import List

from stellar_burgers.bun import Bun
from stellar_burgers.ingredient import Ingredient



class Burger:
    """
    Модель бургера.
    Бургер состоит из булочек и ингредиентов (начинка или соус).
    Ингредиенты можно перемещать и удалять.
    Можно распечать чек с информацией о бургере.
    """

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    # Устанавливает булку для бургера.
    def set_buns(self, bun: Bun):
        self.bun = bun

    # Добавляет ингредиент в бургер.
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    # Удаляет ингредиент из бургера.
    def remove_ingredient(self, index: int):
        del self.ingredients[index]

    # Перемещает ингредиент внутри бургера.
    def move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    # Возвращает общую стоимость бургера.
    def get_price(self) -> float:
        price = self.bun.get_price() * 2

        for ingredient in self.ingredients:
            price += ingredient.get_price()

        return price

    # Возвращает текстовое описание бургера
    def get_receipt(self) -> str:
        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']

        for ingredient in self.ingredients:
            receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')

        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price()}')

        return '\n'.join(receipt)
