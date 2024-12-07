from task import Car, Book, BankAccount  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    book = Book("Under the Dome", "Stephen King", 1024, "фантастика")
    car = Car("Toyota", "Supra A90", 2020, "Red")
    BA = BankAccount(1233113, "Iv KT", 1000)

    try:
        book.remaining_pages("20")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        car.speed_change("10")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
            BA.payment(10000)
    except ValueError:
        print('Ошибка: неправильные данные')
