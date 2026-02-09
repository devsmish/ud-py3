# # built-in functions
# x = print('Hello!')
# y = set()
#
# print(type(x))
# print(type(y))
#
# print(x)
# print(y)
#
# # built-in methods
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)

# def print_greeting():
#     '''
#     Print 'Hello!' text
#     :return: None
#     '''
#     print('Hello!')
#
# # call the function
# print_greeting()
#
# # receive the description of the function
# help(print_greeting)

# def print_greeting_with_name(name = 'Name'):
#     '''
#     :param name
#     :return: None
#     '''
#     print('Hello ' + name + '!')
# print_greeting_with_name('Jack')
# help(print_greeting_with_name)
# print_greeting_with_name()
# x = print_greeting_with_name('Jane')
# print(x)

# def sum_of_two_numbers(a = 0, b = 0):
#     '''
#
#     :param a: The first addend
#     :param b: The second addend
#     :return: Sum of a and b
#     '''
#     return a + b
# x = sum_of_two_numbers(45, 7)
# x = sum_of_two_numbers()
# print(x)
# help(sum_of_two_numbers)

# def is_hello_in_text(text):
#     if 'hello' in text.lower():
#         return True
#     else:
#         return False
# print(is_hello_in_text('Hello everyone!'))

# def is_hello_in_text(text):
#     return 'hello' in text.lower()
#
# print(is_hello_in_text('everyone!'))
#
# def is_string_in_text(string, text):
#     return string in text
# print(is_string_in_text('he', 'The apple'))
# print(is_string_in_text('hey', 'The apple'))

# def greeting_depends_on_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + '! You look great!')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + '! You are so nice!')
#         return gender
#     else:
#         print('Hello ' + name + '! I\'ve never seen the creature like you!')
#         return gender
#
#
# returned_value = greeting_depends_on_gender('Jack', 'male')
# returned_value = greeting_depends_on_gender('Jane', 'female')
# returned_value = greeting_depends_on_gender('Ja', 'cmale')

# def greeting_depends_on_gender(name, gender):
#     if gender == 'male':
#         return gender
#         print('Hello ' + name + '! You look great!')
#     elif gender == 'female':
#         print('Hello ' + name + '! You are so nice!')
#         return gender
#     else:
#         print('Hello ' + name + '! I\'ve never seen the creature like you!')
#         return gender
#
#
# returned_value_1 = greeting_depends_on_gender('Jack', 'male')
# returned_value_2 = greeting_depends_on_gender('Jane', 'female')
# returned_value_3 = greeting_depends_on_gender('Ja', 'cmale')
#
# print(returned_value_1)
# print(returned_value_2)
# print(returned_value_3)

# HOMEWORK
'''1. Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!' соответственно. Сделайте
по одному вызову каждой из функций'''
def cat_voice():
    print('Meow!')

def dog_voice():
    print('Woof!')

cat_voice()
dog_voice()

'''2. Создайте функции cat_voice() and dog_voice(), которые возвращают значения 'Meow!' и 'Woof!' соответственно. 
Выведите на экран 'Meow!' и 'Woof!' по 2 раза'''
def cat_voice():
    print('Meow!')

def dog_voice():
    print('Woof!')

cat_voice()
cat_voice()
dog_voice()
dog_voice()

'''3. Создайте функцию get_voice() которая возвращает передаваемый ей в качестве параметра текст c восклицательным 
знаком.'''
def get_voice(voice):
    print(voice + '!')

voice = input('Enter your voice: ')
get_voice(voice)

'''4. Создайте функцию, которая генерирует последовательность нечетных чисел в диапазоне от a до b (a и b включительно). 
Значения a и b должны передаваться в качестве параметров. Результирующая последовательность должна возвращаться в форме 
объекта list. Решите задание двумя способами - при помощи List Comprehension  и без него'''
def generate_odd_num1(a, b):
    num_list = []
    for num in range(a, b + 1):
        if num % 2 != 0:
            num_list.append(num)
    return num_list

def generate_odd_num2(a, b):
    num_list = [num for num in range(a, b + 1) if num % 2 != 0]
    return num_list

a = int(input('Enter a start number: '))
b = int(input('Enter a end number: '))
print(generate_odd_num1(a, b))
print(generate_odd_num2(a, b))