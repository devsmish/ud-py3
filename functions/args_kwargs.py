# *args and **kwargs

# # *args
# def func_with_args(*args):
#     print(args)
#
#
# func_with_args(1, 2, 3)

# def ten_percent_of_product(x, y, z):
#     return (x * y * z) * 0.1
#
#
# print(ten_percent_of_product(10, 20, 7, 2))

# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1
#
#
# print(ten_percent_of_product_with_args(10, 20, 2, 1, 4, 345))

# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
#
#
# print(percent_of_product_with_args(20, 10, 20, 2, 1, 4, 345))

# # **kwargs
# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
#
# func_with_kwargs(first=1, second=2, third=3)

# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello! What is your name?')
#
#
# hello_with_kwargs(gender='male', age=24, name='Jack')
# hello_with_kwargs(gender='male', age=24)

# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
#     else:
#         print('{}! What is your name?'.format(greeting))
#
#
# hello_with_greeting_and_kwargs('Good morning', gender='male', age=24, name='Jack')
# # hello_with_greeting_and_kwargs(gender='male', age=24)

# def func_with_args_and_kwargs(*args, **kwargs):
#     print('I would like {} {}'.format(args[0], kwargs['food']))
#
# func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')

# HOMEWORK
'''1. Создайте функцию is_cat_here(), которая принимает любое количество аргументов и проверяет есть ли строка 'cat'
среди них. Функция должна возвращать True, если такой параметр есть и False в обратном случае. Буквы в строке 'cat'
могут быть как большие, так и маленькие'''
def is_cat_here(*args):
    for arg in args:
        if 'cat' == str(arg).lower():
            return True
    return False

print(is_cat_here(1, 2 ,3 ,7, True, "False", "CAt", '25'))

'''2. Создайте функцию is_item_here(item, *args), которая проверяет есть ли item среди args. Функция должна возвращать 
True, если такой параметр есть и False в обратном случае.'''
def is_item_here(item, *args):
    for arg in args:
        if item == arg:
            return True
    return False

print(is_item_here(7, '7', "hi", 16, [7, 8], 'False', 7))

'''3. Создайте функцию your_favorite_color() с позиционным параметром my_color и параметрами **kwargs, которая будет 
выводить на экран 'My favorite color is (значение my_color), what is your favorite color?', если в параметрах kwargs нет 
ключа color, и 'My favorite color is (значение my_color), but (значение по ключу color) is also pretty good!', если в 
параметрах kwargs ключ color присутствует'''
def your_favorite_color(my_color, **kwargs):
    for key in kwargs.keys():
        if key == 'color':
            print(f'My favorite color is {my_color}, but {kwargs[key]} is also pretty good!')
            return
    print(f'My favorite color is {my_color}, what is your favorite color?')

your_favorite_color('green', style='casual', color='yellow', pattern='check')