# car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000 }
# print(car_prices)
# print(car_prices['toyota'])
# car_prices['mazda'] = 4000
# print(car_prices)
# car_prices['opel'] = 2000
# print(car_prices)
# del car_prices['toyota']
# print(car_prices)
# # del car_prices
# car_prices.clear()
# print(car_prices)

# person = {
#     'first name': 'Jack',
#     'last name': 'Brown',
#     'age': 43,
#     'hobbies': ['football', 'singing', 'photo'],
#     'children': {'son': 'Michael', 'daugter': 'Pamela'}
# }
#
# print(person['age'])
# print(person['hobbies'])
# hobbies = person['hobbies']
# print(hobbies[2])
#
# print(person['hobbies'][2])
#
#
# children = person['children']
# print(children['son'])
#
# print(person['children']['son'])
#
# person['car'] = 'Mazda'
# person['hobbies'][0] = 'basketball'
#
# print(person.keys())
# print(person.values())
# print(person.items())

# HOMEWORK
'''Вопросы к этому заданию
1. Создайте объект dictionary, содержащий пары ключей и значений, выведите на экран одно значение
2. Создайте объект dictionary, описывающий компьютер'''
dictionary = {'car': 'автомобиль', 'bus': 'автобус', 'tram': 'трамвай', 'train': 'поезд', 'rocket': 'ракета'}
print(dictionary['bus'])

descr_pc = {'cpu': {'model': "Intel Core i9", 'frequency': "3,5 GHz", 'count_core': 8}, 'motherboard': 'ASUS P7-1402',
            'RAM': {'memory': "64 Gb", 'type': "DDR5"}, 'SSD size': "1 Tb", 'HDD size': "4 Tb", 'OS': 'Windows11 Home',
            'connectors': {'USB 3.0': 2, 'USB-C': 4, 'Type-C': 2, 'HDMI': 1, 'Ethernet': 1},
            'peripherals': ['Display', {'resolution': '1920x1080 Full HD', 'wireless': ['Wi-Fi', 'Bluetooth 5.0']}]}