from functools import wraps


def print_function_data(function):
    """
    This is decorator function
    :param function:
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    """

    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    """
    return a * a + b * b


# print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
help(squares_sum)

# HOMEWORK
"""Создайте функцию-декоратор print_args, которая распечатывает аргументы *args и **kwargs функции, которую она 
декорирует"""
from functools import wraps


def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return wrapper

@print_args
def squares_sum(name, list_drinks, foods):
    return print("Все аргументы напечатаны")

name = "Rafael"
list_drinks = ["Tee", "Coffee", "Limonad"]
foods = {'Pizza': 'ITA', 'Julien': 'FRA', 'Burito': 'MEX', 'Doner': 'TUR'}

squares_sum(name, list_drinks, foods=foods)