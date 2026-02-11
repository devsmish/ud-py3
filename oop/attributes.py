# class Car:
#
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#
# mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)
#
# print(mazda_car.name)
# print(mazda_car.is_crashed)
# print(mazda_car.wheels_number)
#
# bmw_car = Car(name='BMW', color='black', year=2018, is_crashed=False)
#
# print(bmw_car.name)
# print(bmw_car.year)
# print(bmw_car.wheels_number)

# HOMEWORK
# Создайте класс BlogPost с атрибутами user_name, text, number_of_likes. Создайте два объекта этого класса. После
# создания измените атрибут number_of_likes одного из объектов. Распечатайте атрибут number_of_likes каждого из объектов
class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

customer = BlogPost(user_name='Jake', text='He favorite color is blue', number_of_likes=7)
client = BlogPost(user_name='Janet', text='She favorite color is rosa', number_of_likes=25)
customer.number_of_likes = 16
print(customer.number_of_likes)
print(client.number_of_likes)