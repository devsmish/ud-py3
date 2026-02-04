# tuple_1 = 1, 2, 3
# tuple_2 = ('one', 'hello')
# tuple_3 = (3, 2.3, 'three')
#
# # tuple_1[1] = 3
#
# new_tuple = (tuple_1[0], 3, tuple_1[-1])
# print(new_tuple)
#
# print(tuple_1[1])
# print(type(tuple_1))
# print(tuple_2)
# print(tuple_3)

# x = y = z = 12
# x, y, z = 12, 13, 14
#
# print(x, y, z)
#
# person_tuple = ('John', 'Smith', 1986)
# first_name, last_name, year_of_birth = person_tuple
#
# print(first_name, last_name, year_of_birth)
#
# t1 = (1, 2, 5, 1, 7, 9)
# print(t1.count(5))
#
# greetings_tuple = ('hello', 'hi', 'hey', 'hi')
# print(greetings_tuple.count('hola'))
#
# print(t1.index(1))
# print(greetings_tuple.index('hi'))

# HOMEWORK
'''Создайте объект tuple, описывающий компьютер и распакуйте его в соответствующие переменные. Выведите переменные
вызвав функцию print() один раз'''
descr_pc = ("Intel Core i9 3,5 GHz 8 core", 'ASUS P7-1402', "DDR5 64 Gb", "1 Tb", "4 Tb", 'Windows11 Home',
            "USB 3.0, Type-C, HDMI, Ethernet")
cpu = motherboard = ram = ssd = hdd = op_sys = connectors = ''
cpu, motherboard, ram, ssd, hdd, op_sys, connectors = descr_pc
print(f"Описание компьютера:\n процессор {cpu}\n материнская плата {motherboard}\n ОЗУ {ram}\n SSD-диск {ssd}\n \
HDD-диск {hdd}\n операционная система {op_sys}\n разъемы: {connectors}.")