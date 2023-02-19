import doctest


class Room:
    def __init__(self, length: int, width: int, height: int):
        """
        Создание и подготовка к работе объекта "Комната"

        :param length: Длина комнаты, мм
        :param width: Ширина комнаты, мм
        :param height: Высота комнаты, мм

        Примеры:
        >>> kitchen = Room(3200, 2100, 2700)  # инициализация экземпляра класса
        """
        if not isinstance(length, int):
            raise TypeError("Длина должна быть типа int")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, int):
            raise TypeError("Ширина должна быть типа int")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("Высота должна быть типа int")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def area(self) -> float:
        """
        Функция, которая вычисляет площадь комнаты в кв. м

        :return: Площадь комнаты, кв. м

        Примеры:
        >>> kitchen = Room(3200, 2100, 2700)
        >>> kitchen.area()
        6.72
        """
        return self.length * self.width / 10 ** 6

    def perimeter(self) -> float:
        """
        Функция, которая вычисляет периметр комнаты в м

        :return: Периметр комнаты, м

        Примеры:
        >>> kitchen = Room(3200, 2100, 2700)
        >>> kitchen.perimeter()
        10.6
        """
        return (self.length + self.width) * 2 / 10 ** 3


class Basket:
    def __init__(self, cost: int, products_amount: int):
        """
        Создание и подготовка к работе объекта "Корзина"

        :param cost: Стоимость товаров в корзине, руб
        :param products_amount: Количество товаров в корзине

        Примеры:
        >>> basket1 = Basket(2399, 3)  # инициализация экземпляра класса
        """
        if not isinstance(cost, int):
            raise TypeError("Стоимость должна быть целочисленным значением")
        if cost <= 0:
            raise ValueError("Стоимость должна быть положительным значением")
        self.cost = cost

        if not isinstance(products_amount, int):
            raise TypeError("Количество товаров должно быть целочисленным значением")
        if products_amount <= 0:
            raise ValueError("Количество товаров должно быть положительным значением")
        self.products_amount = products_amount

    def delete_product_from_basket(self, product: str) -> None:
        """
        Удаление товара из корзины

        :param product: Удаляемый из корзины товар
        :raise ValueError: Если такого товара в корзине нет, то возвращается ошибка

        Примеры:
        >>> basket1 = Basket(2399, 13)
        >>> basket1.delete_product_from_basket("Хлеб")
        """
        ...

    def is_empty_basket(self) -> bool:
        """
        Функция, которая проверяет, пустая корзина или нет

        :return: пустая корзина или нет

        Примеры:
        >>> basket1 = Basket(2399, 13)
        >>> basket1.is_empty_basket()
        """
        ...


class Car:
    def __init__(self, name: str, cost: int, color: str):
        """
        Создание и подготовка к работе объекта "Машина"

        :param name: Марка машины
        :param cost: Стоимость машины, руб
        :param color: Цвет машины

        Примеры:
        >>> car1 = Car("BMW", 2800000, "Черный")  # инициализация экземпляра класса
        """
        self.name = name
        self.color = color
        if not isinstance(cost, int):
            raise TypeError("Стоимость должна быть целочисленным значением")
        if cost <= 0:
            raise ValueError("Стоимость должна быть положительным значением")
        self.cost = cost

    def repaint(self, new_color: str) -> None:
        """
        Покраска машины

        :param new_color: Новый цвет машины

        Примеры:
        >>> car1 = Car("BMW", 2800000, "Черный")
        >>> car1.repaint("Белый")
        """
        self.color = new_color

    def wash(self) -> None:
        """
        Мойка машины

        Примеры:
        >>> car1 = Car("BMW", 2800000, "Черный")
        >>> car1.wash()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

