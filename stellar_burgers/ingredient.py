class Ingredient:
    """
    Модель ингредиента.
    Ингредиент: начинка или соус.
    У ингредиента есть тип (начинка или соус), название и цена.
    """

    def __init__(self, ingredient_type: str, name: str, price: float):
        if not ingredient_type:
            raise ValueError("Тип ингредиента не может быть пустым.")
        if not name:
            raise ValueError("Имя не может быть пустым.")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type

    # Возвращает строковое представление ингредиента. Формат: "ТИП: название ($цена)"
    def __str__(self) -> str:
        return f"{self.type}: {self.name} (${self.price})"
