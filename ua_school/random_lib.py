from random import*
s = 0
k = 0

while s <= 18:
        x = randint(1, 6)
        print(x)
        s = s + x
        k = k + 1

print("Кількість k = ", k, "Сума s = " , s)