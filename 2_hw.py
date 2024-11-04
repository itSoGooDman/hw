def task_1() -> None:
    # Создаём переменные с разными типами данных
    var_int = 10  # int
    var_float = 3.14  # float
    var_str = "Hello, world!"  # str
    var_list = [1, 2, 3, 4, 5]  # list
    var_bool = True  # bool

    # Выводим тип данных каждой переменной
    print("Тип var_int:", type(var_int))
    print("Тип var_float:", type(var_float))
    print("Тип var_str:", type(var_str))
    print("Тип var_list:", type(var_list))
    print("Тип var_bool:", type(var_bool))


# Вызов функции
task_1()


def task_2() -> None:
    # Создаем список
    a = [1, 2, 3, 5, 8, 13, 21]

    # Выводим первые три элемента списка
    print("Первые три значения списка:", a[:3])


# Вызов функции
task_2()



def task_3(number: int) -> int:
    # Возвращаем квадрат числа
    return number ** 2

# Вызов функции с выводом в консоль
print("Квадрат числа 5:", task_3(5))
