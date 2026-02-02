greeting = 'Hello Python!'
greeting_length = len(greeting)
print(len(greeting))

# Indexing
print(greeting[1])
print(greeting[6])
print(greeting[-1])
print(greeting[12])
print(greeting[-4])

# Slicing
print(greeting[2:5])
print(greeting[6:10])
print(greeting[2:5])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[:5])
print(greeting[:])
print(greeting[::2])
print(greeting[::1])
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1])

# homework
'''Вопросы к этому заданию
1. Выведите на печать вторую букву l из строки 'Hello Python!'
Присвойте строку переменной, затем выведите на печать букву
2. Выведите на печать вторую букву l из строки 'Hello Python!'. Сделайте это без присваивания строки переменной, в 
одной строке кода. Если не знаете, как это сделать, попробуйте погуглить
3. Выведите на печать 'He' из строки 'Hello Python!' минимум двумя способами
4. Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации части строки и отсутствующего символа. 
Выведите новую строку на печать'''
text = 'Hello Python!'
print(text[3])

print('Hello Python!'[3])

print(text[0:2])
print(text[:2])
print(text[0:2:1])
print(text[-13:-11])

text_concat = text[6] + 'a' + text[-5:-3]
print(text_concat)