class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    def __str__(self):
        return f"Бумажная книга {self.__name}. Автор {self.__author}. {self.pages} страниц."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должно быть целым числом.')
        if pages <= 0:
            raise ValueError('Число страниц не может быть меньше или равно 0.')
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Длительность {self.duration} часов."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, au  thor={self.__author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def duration(self, duration: int) -> None:
        if not isinstance(duration, int):
            raise TypeError('Продолжительность аудиокниги должна быть типа float.')
        if duration <= 0:
            raise ValueError('Продолжительность аудиокниги не может быть меньше или равна 0.')
        self.duration = duration
