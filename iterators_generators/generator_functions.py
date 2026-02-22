# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions


# def my_function(x):
#     return x
#
#
# print(my_function(4))


def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


# print(count_up_to(4))
# counter = count_up_to(4)
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

counter = count_up_to(10)
print(list(count_up_to(7)))

# for number in counter:
#     print(number)

counter.__next__()
counter.__next__()
counter.__next__()

for number in counter:
    print(number)

# HOMEWORK
"""Создайте функцию-генератор get_week_day(), которая создаёт генератор, вырабатывающий один день недели за раз, Дни 
недели должны начинаться с воскресенья и заканчиваться субботой.
current_day = get_week_day()
print(current_day.__next__()) # 'Sunday'
print(current_day.__next__()) # 'Monday'
print(current_day.__next__()) # 'Tuesday'
print(current_day.__next__()) # 'Wednesday'
print(current_day.__next__()) # 'Thursday'
print(current_day.__next__()) # 'Friday'
print(current_day.__next__()) # 'Saturday'"""
def get_week_day():
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for item in day_list:
        yield item

current_day = get_week_day()

print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())

"""Создайте функцию even_odd(), создающую генератор, который будет попеременно вырабатывать строки 'even' и 'odd'.
even_odd_generator = even_odd()
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'"""
def even_odd():
    while True:
        yield 'even'
        yield 'odd'

even_odd_generator = even_odd()

print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))