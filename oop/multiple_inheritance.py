class Swimmable:
    def __init__(self, name):
        print('Method init() of Swimmable class')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can swim')

    def swim(self):
        print("I'm swimming")

class Walkable:
    def __init__(self, name):
        print('Method init() of Walkable class')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can walk')

    def walk(self):
        print("I'm walking")

class Flyable:
    def __init__(self, name):
        print('Method init() of Flyable class')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can fly')

    def fly(self):
        print("I'm flying")

class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        print('Method init() of GameCharacter class')
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    def greeting(self):
        print(f'Hello! My name is {self.name}')

james = Swimmable('James')
james.greeting()

james2 = GameCharacter('James')
james2.greeting()

james.swim()
james2.swim()
james2.walk()
james2.fly()

print(isinstance(james, Walkable))
print(isinstance(james2, Swimmable))
print(isinstance(james2, Walkable))
print(isinstance(james2, Flyable))
print(isinstance(james2, GameCharacter))
print(isinstance(james2, dict))
print(isinstance(james, object))