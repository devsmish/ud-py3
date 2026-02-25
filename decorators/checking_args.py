# from functools import wraps
#
#
# def prohibit_kwargs(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError('Keyword arguments are prohibited')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def prohibit_int_arguments(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for val in args:
#             if type(val) == int:
#                 raise ValueError('Integer arguments are prohibited')
#         for key, val in kwargs.items():
#             if type(val) == int:
#                 raise ValueError('Integer arguments are prohibited')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @prohibit_int_arguments
# def print_hello(name):
#     print(f'Hello {name}!')
#
#
# print_hello('Jack')
# print_hello(3)

# HOMEWORK
'''Создайте функцию-декоратор prohibit_more_than_2_args, которая выполняет функцию, которую она декорирует, если в этой
функции не больше двух аргументов. В противном случае должна вызываться ошибка ValueError с сообщением "Function must 
have less than 3 arguments!"'''
from functools import wraps

def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) > 2:
            raise ValueError("Function must have less than 3 arguments!")
        return func(*args, **kwargs)
    return wrapper

a = 5
b = 2
c = {1: 1, 2: 2, 3: 3}
@prohibit_more_than_2_args
def add_two_numbers():
    return a + b

add_two_numbers(a, b, c)