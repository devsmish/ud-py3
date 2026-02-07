number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
#     print(str(number) + ' Hola!')

# for number in number_list:
#     if number % 2 == 0:
#         print(number)
#     else:
#         print('Hey!')

# list_numbers_sum = 0
# for number in number_list:
#     list_numbers_sum = list_numbers_sum + number
# print(list_numbers_sum)

# greeting = 'Hello Python!'
# for letter in greeting:
#     print(letter)

# greeting = 'Hello Python!'
# for letter in greeting:
#     if letter != 'o':
#         print(letter)

# for letter in 'Hello Python!':
#     if letter != 'o':
#         print(letter)

# for letter in 'Hello Python!':
#     print('One more letter!')

# tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list:
#     print(item)
# for letter_1, letter_2 in tuple_list:
#     print(letter_1, letter_2)
# for letter_1, letter_2 in tuple_list:
#     print(letter_1)

# tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
# for letter_1, letter_2, number in tuple_list_1:
#     print(letter_1, letter_2, number)

# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#
# # key-value pairs in tuples
# for item in dictionary.items():
#     print(item)
#
# # keys
# for item in dictionary:
#     print(item)
# for item in dictionary.keys():
#     print(item)
# for key, value in dictionary.items():
#     print(key)
#
# # values
# for item in dictionary.values():
#     print(item)
# for key, value in dictionary.items():
#     print(value)

# for _ in range(5):
#     print('Hello!')

# HOMEWORK
'''1. Используйте цикл for для вычисления суммы всех чётных чисел в диапазоне от 10 до 30 (включая крайние значения).
Выведите результат на печать

2. Получите от пользователя число на вводе и используйте цикл for для вывода на экран текста 'Hello!' столько же раз'''
result = 0
for number in range(10, 31):
    if number % 2 == 0:
        result += number
print(result)

str_count = int(input('Enter a integer number: '))
for count in range(1, str_count + 1):
    print("Hello!")