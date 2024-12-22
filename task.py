class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def get_name(self):
        return self._name

    def set_name(self, value):
        raise AttributeError("Название книги нельзя изменить")

    def get_author(self):
        return self._author

    def set_author(self, value):
        raise AttributeError("Автора книги нельзя изменить")

    name = property(get_name, set_name)
    author = property(get_author, set_author)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(name={self.name!r}, "
            f"author={self.author!r})"
        )


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def get_pages(self):
        return self._pages

    def set_pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    pages = property(get_pages, set_pages)

    def __str__(self):
        return f"{super().__str__()} Страниц: {self.pages}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(name={self.name!r}, "
            f"author={self.author!r}, pages={self.pages})"
        )


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def get_duration(self):
        return self._duration

    def set_duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Продолжительность должна быть числом с плавающей запятой")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = value

    duration = property(get_duration, set_duration)

    def __str__(self):
        return f"{super().__str__()} Продолжительность: {self.duration:.2f} часа"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(name={self.name!r}, "
            f"author={self.author!r}, duration={self.duration:.2f})")
