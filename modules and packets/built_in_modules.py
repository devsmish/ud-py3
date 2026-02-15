# import random
# x = random.randint(1, 10)
# print(x)

# from random import randint
# x = randint(1, 10)
# print(x)
#
# from random import shuffle
# my_list = [1,2,3]
# shuffle(my_list)
# print(my_list)

from random import shuffle as shuffle_my_list
my_list = [1,2,3]
shuffle_my_list(my_list)
print(my_list)

# HOMEWORK
'''Импортируйте встроенный модуль math. Вычислите при помощи функций этого модуля:
1. Корень квадратный из числа 123456789
2. Факториал числа 987
3. 876 в степени 54'''
import math

a = 123456789
b = 987
c = 876

print(math.sqrt(a))
print(math.factorial(b))
print(math.pow(c, 54))