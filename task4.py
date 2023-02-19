import doctest


class Shoes:
    def __init__(self, size: int, color: str, material: str):
        """
        Создание и подготовка к работе объекта "Обувь"

        :param size: Размер обуви
        :param color: Цвет обуви
        :param material: Материал, из которого изготовлена обувь

        Примеры:
        >>> boots = Shoes(42, "Черный", "Кожа")
        """
        self.size = size  # добавляем проверку по типу и значению
        self.color = color
        self.material = material

    @property
    def size(self) -> int:
        """Возвращает размер обуви"""
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        """Устанавливает размер обуви"""
        if not isinstance(new_size, int):
            raise TypeError("Размер обуви должен быть типа int")
        if new_size <= 0:
            raise ValueError("Размер обуви должен быть положительным числом")
        self._size = new_size

    def is_clean_shoes(self) -> bool:
        """
        Метод, проверяющий, чистая ли обувь

        :return: чистая ли обувь

        Примеры:
        >>> boots = Shoes(42, "Черный", "Кожа")
        >>> boots.is_clean_shoes()
        """
        ...

    def find_shoes(self) -> None:
        """
        Метод, который находит обувь в интернет-магазине

        Примеры:
        >>> boots = Shoes(42, "Черный", "Кожа")
        >>> boots.find_shoes()
        """
        ...

    def __str__(self) -> str:
        return f"Обувь {self.size} размера. Цвет - {self.color}. Материал - {self.material}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self.size}, color={self.color!r}, material={self.material!r})"


class Sneakers(Shoes):
    def __init__(self, brand: str, size: int, color: str, material: str):
        """
        Создание и подготовка к работе объекта "Кроссовки"

        :param brand: Бренд кроссовок
        :param size: Размер кроссовок
        :param color: Цвет кроссовок
        :param material: Материал, из которого изготовлены кроссовки

        Примеры:
        >>> sneakers1 = Sneakers("Nike", 39, "Белый", "Ткань")
        """
        super().__init__(size, color, material)
        self.brand = brand

    def find_shoes(self) -> None:
        """
        Метод, который находит обувь в интернет-магазине
        Перегружаем метод, чтобы отфильтровать интернет-магазины, среди которых нужно вести поиск (спортивные магазины)

        Примеры:
        >>> sneakers1 = Sneakers("Nike", 39, "Белый", "Ткань")
        >>> sneakers1.find_shoes()
        """
        ...

    def __str__(self) -> str:
        # Перегружаем метод, чтобы добавить название бренда кроссовок
        return f"Кроссовки {self.brand} {self.size} размера. Цвет - {self.color}. Материал - {self.material}"

    def __repr__(self) -> str:
        # Перегружаем метод, чтобы добавить атрибут brand, необходимый для инициализации экземпляра
        return f"{self.__class__.__name__}(brand={self.brand!r}, size={self.size}, color={self.color!r}, material={self.material!r})"


if __name__ == "__main__":
    doctest.testmod()

