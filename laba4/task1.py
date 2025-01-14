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
        self._make = make
        self._model = model
        self._year_of_manufacture = year_of_manufacture

    def get_make(self) -> str:
        """Возвращает марку автомобиля."""
        return self._make

    def set_make(self, new_make: str):
        """Устанавливает новую марку автомобиля."""
        if not isinstance(new_make, str):
            raise TypeError("Марка должна быть строкой.")
        self._make = new_make

    def get_model(self) -> str:
        """Возвращает модель автомобиля."""
        return self._model

    def set_model(self, new_model: str):
        """Устанавливает новую модель автомобиля."""
        if not isinstance(new_model, str):
            raise TypeError("Модель должна быть строкой.")
        self._model = new_model

    def get_year_of_manufacture(self) -> int:
        """Возвращает год выпуска автомобиля."""
        return self._year_of_manufacture

    def set_year_of_manufacture(self, new_year_of_manufacture: int):
        """Устанавливает новый год выпуска автомобиля."""
        if not isinstance(new_year_of_manufacture, int):
            raise TypeError("Год выпуска должен быть целым числом.")
        self._year_of_manufacture = new_year_of_manufacture

    def greeting(self) -> None:
        """Приветственное сообщение при создании экземпляра автомобиля."""
        print(f"Привет! Я {self._make} {self._model}, выпущенный в {self._year_of_manufacture}.")

    def __str__(self) -> str:
        """Строковое представление автомобиля."""
        return f"{self._make} {self._model} ({self._year_of_manufacture})"

    def __repr__(self) -> str:
        """Представление автомобиля для разработчиков."""
        return f'Car({self._make!r}, {self._model!r}, {self._year_of_manufacture!r})'

# TODO: описать дочерний класс


class Sedan(Car):
    """Дочерний класс для описания легковых автомобилей."""

    def __init__(self, make: str, model: str, year_of_manufacture: int, number_of_seats: int):
        """
        Конструктор класса sedan.

        :param make: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year_of_manufacture: Год выпуска легкового автомобиля.
        :param number_of_seats: Количество мест в автомобиле.
        """
        super().__init__(make, model, year_of_manufacture)
        self._number_of_seats = number_of_seats

    def get_number_of_seats(self) -> int:
        """Возвращает количество мест в легковом автомобиле."""
        return self._number_of_seats

    def set_number_of_seats(self, new_number_of_seats: int):
        """Устанавливает новое количество мест в легковом автомобиле."""
        if not isinstance(new_number_of_seats, int):
            raise TypeError("Количество мест должно быть целым числом.")
        self._number_of_seats = new_number_of_seats

    def greeting(self) -> None:
        """Перегруженное приветственное сообщение для легкового автомобиля."""
        # Перегрузка метода для включения информации о количестве мест
        print(
            f"Привет! Я {self._make} {self._model}, выпущенный в {self._year_of_manufacture}. У "
            f"меня есть {self._number_of_seats} места.")

    def __str__(self) -> str:
        """Строковое представление легкового автомобиля."""
        return f"{super().__str__()} (количество мест: {self._number_of_seats})"

    def __repr__(self) -> str:
        """Представление легкового автомобиля для разработчиков."""
        return f'sedan({self._make!r}, {self._model!r}, {self._year_of_manufacture!r}, {self._number_of_seats!r})'

# Создание экземпляра базового класса


auto = Car('Toyota', 'Corolla', 2020)
auto.greeting()  # Toyota Corolla (2020)


# Создание экземпляра дочернего класса
legkovushka = Sedan('Mercedes-Benz', 'C-Class', 2018, 4)
legkovushka.greeting()  # Mercedes-Benz C-Class (2018) (количество мест: 4)
