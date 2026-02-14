# Определение порядка наследования классов и порядка выполнения их общих методов

#     A
#    / \
#   B   C
#    \ /
#     D
class A:
    def some_method(self):
        print('Method of class A')

class B(A):
    def some_method(self):
        print('Method of class B')

class C(A):
    def some_method(self):
        print('Method of class C')

class D(B, C):
    @classmethod # если для метода не используются параметры, которые могут иметь разные значения,
# тогда такой метод можно определять как метод уровня класса
    def some_method(cls):
        print('Method of class D')

# __mro__, mro(), help()
print(D.__mro__)
print(D.mro())
help(D)

some_object = D()
some_object.some_method()