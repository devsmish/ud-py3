# List Comprehension
# greeting = 'hello!'
# letter_list = []
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)

# letter_list = [letter for letter in greeting]
# print(letter_list)
# number_list = [number for number in '0123456789']
# print(number_list)
# number_list_1 = [num for num in range(0, 10)]
# print(number_list_1)
# number_list_2 = [num ** 2 for num in range(0, 10)]
# print(number_list_2)
# number_list_3 = [- ((num - 3) / 2) ** 2 for num in range(0, 10)]
# print(number_list_3)

# number_list = [6, 43, -2, 11, -55, -12, 3, 345, 0]
# new_list = [number ** 3 / 2 for number in number_list if number > 0]
# print(new_list)
# new_list_1 = ['+' if number > 0 else '-' if number < 0
#               else 'zero' for number in number_list]
# print(new_list_1)

# # Dictionary Comprehension
# number_dict = {'first': 1, 'second': 2, 'third': 3}
# new_dict = {key: value ** 3 for key, value in number_dict.items()}
# print(new_dict)
#
# number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
# number_dict = {number: number ** 2 for number in number_list}
# print(number_dict)
# number_dict = {number: 'positive' if number > 0
# else 'negative' if number < 0 else 'zero' for number in number_list}
# print(number_dict)

# Set Comprehension
# number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
# number_set = {number ** 2 for number in number_list}
# print(number_set)
# number_set = {number ** 2 for number in range(3, 11)}
# print(number_set)
# letter_set = {letter.upper() for letter in 'hello'}
# print(letter_set)

# HOMEWORK
'''Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola'] создайте новый список содержащий вторую букву из
каждой строки исходного списка. Выведите новый список на печать. Решите задание двумя способами - при помощи List
Comprehension и без него.

Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создайте новый список содержащий нечетные числа исходного
списка. Выведите новый список на печать. Решите задание двумя способами - при помощи List Comprehension и без него.'''
greetings = ['hello', 'hi', 'hey', 'hola']
res_list1 = []
for string in greetings:
    res_list1 = res_list1 + list(string[1])
print(res_list1)

res_list2 = [string[1] for string in greetings]
print(res_list2)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dig_list1 = []
for digit in digits:
    if digit % 2 != 0:
        dig_list1 = dig_list1 + [digit]
print(dig_list1)

dig_list2 = [digit for digit in digits if digit % 2 != 0]
print(dig_list2)