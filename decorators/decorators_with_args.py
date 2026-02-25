from functools import wraps

#
# def check_if_first_arg_is(value):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != value:
#                 print(f'First argument has to be {value}')
#             return func(*args, **kwargs)
#         return wrapper
#     return inner_dec
#
#
# @check_if_first_arg_is('red')
# def print_rainbow_colors(*colors):
#     print(colors)
#
#
# @check_if_first_arg_is(7)
# def multiply_7(a, b):
#     return a * b
#
#
# print_rainbow_colors('orange', 'yellow', 'green', 'blue',
#                      'indigo', 'violet')
#
# print(multiply_7(7, 3))


def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', '3')

# *args - ('Hi!', '3')
# *types - (str, int)
# zip(args, types) - ('Hi!', str) ('3', int)


@enforce(float, float)
def divide(a, b):
    return a / b


print(divide(4, 2))
print(divide('4', '2'))

# HOMEWORK
'''Создайте функцию-декоратор wait, которая задерживает выполнение кода функции, которую она декорирует, на n секунд. 
Аргумент n должен передаваться в декоратор. Воспользуйтесь функцией для задержки выполнения кода. Найдите информацию об 
использовании этой функции в интернете самостоятельно. Также после задержки должно выводится сообщение "There was a 
pause {количество секунд} seconds before execution {имя задекорированной функции }"'''
from functools import wraps
import time

def wait(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(n)
            print(f"There was a pause {n} seconds before execution {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@wait(3)
def divider(a, b):
    return a / b

divider(14, 2)