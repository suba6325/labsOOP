# TODO: описать базовый класс


class Car:
    """Базовый класс для описания автомобилей."""

    def __init__(self, make: str, model: str, year_of_manufacture: int):
        """
        Конструктор класса Car.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year_of_manufacture: Год выпуска автомобиля.
        """
        self.make = make
        self.model = model
        self.year_of_manufacture = year_of_manufacture

    @property
    def make(self) -> str:
        """Возвращает марку автомобиля."""
        return self._make

    @make.setter
    def make(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Марка должна быть строкой.")
        self._make = value

    @property
    def model(self) -> str:
        """Возвращает модель автомобиля."""
        return self._model

    @model.setter
    def model(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Модель должна быть строкой.")
        self._model = value

    @property
    def year_of_manufacture(self) -> int:
        """Возвращает год выпуска автомобиля."""
        return self._year_of_manufacture

    @year_of_manufacture.setter
    def year_of_manufacture(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Год выпуска должен быть целым числом.")
        self._year_of_manufacture = value

    def greeting(self) -> None:
        """Приветственное сообщение при создании экземпляра автомобиля."""
        print(f"Привет! Я {self.make} {self.model}, выпущенный в {self.year_of_manufacture}.")

    def __str__(self) -> str:
        """Строковое представление автомобиля."""
        return f"{self.make} {self.model} ({self.year_of_manufacture})"

    def __repr__(self) -> str:
        """Представление автомобиля для разработчиков."""
        return f'Car({self.make!r}, {self.model!r}, {self.year_of_manufacture!r})'


# TODO: описать дочерний класс


class Sedan(Car):
    """Дочерний класс для описания легковых автомобилей."""

    def __init__(self, make: str, model: str, year_of_manufacture: int, number_of_seats: int):
        """
        Конструктор класса Sedan.

        :param make: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year_of_manufacture: Год выпуска легкового автомобиля.
        :param number_of_seats: Количество мест в автомобиле.
        """
        super().__init__(make, model, year_of_manufacture)
        self.number_of_seats = number_of_seats

    @property
    def number_of_seats(self) -> int:
        """Возвращает количество мест в легковом автомобиле."""
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество мест должно быть целым числом.")
        self._number_of_seats = value

    def greeting(self) -> None:
        """Перегруженное приветственное сообщение для легкового автомобиля."""
        # Перегрузка метода для включения информации о количестве мест
        print(
            f"Привет! Я {self.make} {self.model}, выпущенный в {self.year_of_manufacture}."
            f"У меня есть {self.number_of_seats} места.")

    def __str__(self) -> str:
        """Строковое представление легкового автомобиля."""
        return f"{super().__str__()} (количество мест: {self.number_of_seats})"

    def __repr__(self) -> str:
        """Представление легкового автомобиля для разработчиков."""
        return f'Sedan({self.make!r}, {self.model!r}, {self.year_of_manufacture!r}, {self.number_of_seats!r})'
# Создание экземпляра базового класса


auto = Car('Toyota', 'Corolla', 2020)
auto.greeting()  # Toyota Corolla (2020)


# Создание экземпляра дочернего класса
sedan = Sedan('Mercedes-Benz', 'C-Class', 2018, 4)
sedan.greeting()  # Mercedes-Benz C-Class (2018) (количество мест: 4)
