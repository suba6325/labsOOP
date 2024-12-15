# TODO: Подробно описать три произвольных класса

# TODO: описать класс

class Book:
    def __init__(self, title: str, author: str, pages: int, genre: str):

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        allowed_genres = ["роман", "детектив", "фантастика", "триллер"]
        if genre not in allowed_genres:
            raise ValueError(
                f"Жанр '{genre}' недопустим. Допустимые жанры: {', '.join(allowed_genres)}."
            )

        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def get_info(self) -> None:
        """
          Класс для представления книги.

          >>> book = Book('Война и мир', 'Лев Толстой', 1225, 'роман')
          >>> book.get_info()
          Война и мир автор: Лев Толстой
        """
        print(f"{self.title} автор: {self.author}")

    def remaining_pages(self, pages_to_read: int = 0) -> int:
        """
        >>> book = Book('Война и мир', 'Лев Толстой', 1225, 'роман')
        >>> book.remaining_pages(500)
        725
        """
        if pages_to_read > self.pages:
            raise ValueError("Вы пытаетесь прочитать больше страниц, чем есть в книге.")
        self.pages -= pages_to_read
        return self.pages


# TODO: описать ещё класс


class Car:
    def __init__(self, brand: str, model: str, year: int, color: str):

        if year <= 0 or year > 2025:
            raise ValueError("Год выпуска введен неверно.")

        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.is_running = False

    def start_engine(self) -> None:
        """
        >>> car = Car('Toyota', 'Corolla', 2010, 'white')
        >>> car.start_engine()
        Двигатель запущен.
        """
        if not self.is_running:
            self.is_running = True
            print("Двигатель запущен.")
        else:
            print("Двигатель уже запущен.")

    def stop_engine(self) -> None:
        """
        Класс для представления автомобиля.

        >>> car = Car('Toyota', 'Corolla', 2010, 'white')
        >>> car.start_engine()
        Двигатель запущен.
        >>> car.stop_engine()
        Двигатель остановлен.
        """
        if self.is_running:
            self.is_running = False
            print("Двигатель остановлен.")
        else:
            print("Двигатель уже остановлен.")

    def speed_change(self, delta_speed: int) -> int:
        """
        Класс для представления автомобиля.

        >>> car = Car('Toyota', 'Corolla', 2010, 'white')
        >>> car.speed_change(50)
        50
        """
        if not isinstance(delta_speed, int):
            raise TypeError("Ускорение должно быть типа int")

        new_speed = self.speed + delta_speed
        if new_speed > 130:
            self.speed = 130
            print("Достигли максимальной скорости.")
        if new_speed <= 0:
            self.speed = 0
            print("Вы остановились.")
        else:
            self.speed = new_speed
            return self.speed


# TODO: и ещё один


class BankAccount:
    def __init__(self, account_number: int, owner: str, initial_balance: float = 0.0, currency: str = "RUB"):

        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Начальный баланс должен быть типа int или float")

        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.currency = currency

    def deposit(self, amount: float) -> float:
        """Возвращает баланс после пополнения"""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма пополнения должна быть типа int или float")
        self.balance += amount
        return self.balance

    def payment(self, amount: float) -> float:
        """Возвращает баланс после платежа"""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма снятия должна быть типа int или float")
        new_balance = self.balance - amount
        if new_balance < 0:
            raise ValueError("Сумма снятие не должна превышать баланс")
        else:
            self.balance = new_balance
        return self.balance


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
