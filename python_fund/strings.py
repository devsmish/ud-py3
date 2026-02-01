greeting = 'Hello'
first_name = 'Jack'
last_name = 'White'
exclamation_sign = '!'
white_space = ' '
full_name = first_name + ' ' + last_name
print(greeting + white_space + full_name + exclamation_sign)

whole_sentence = (greeting + white_space + full_name + exclamation_sign)
print(whole_sentence + '!!')

long_string = "This is the long string"
print(long_string)

# Escaping
some_string = "I'm a programmer"
print(some_string)
another_string = 'I want to learn "Python"'
print(another_string)
some_string = 'I\'m a programmer'
print(some_string)
another_string = "I want to learn \"Python\""
print(another_string)

string_with_new_lines = "Hello!\n     \rI love Python"
print(string_with_new_lines)
numbers = "1\t23\t456"
print(numbers)

# Triple quotes
string_with_triple_quotes = """This is text with "triple quotes" """
print(string_with_triple_quotes)
another_string_with_triple_quotes = """This is text with "triple quotes" """
print(another_string_with_triple_quotes)
text_with_triple_quotes = """This is 
text with 
"triple quotes" """
print(text_with_triple_quotes)

# homework
'''Создайте переменные, поместите в них значения - имя, фамилию и возраст. Выведите на экран следующее предложение: 
"Hi! My name is имя фамилия, I'm возраст years old." Используйте конкатенацию переменных и строк.'''
first_name = 'Sergey'
last_name = "Bradobrey"
age = '34'
string_presentation = "Hi! My name is " + first_name + " " + last_name + \
                      ", I\'m " + age + " " + "years old."
print(string_presentation)

'''Выведите на экран текст детской песенки:
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full

One for the master,
One for the dame,
And one for the little boy
Who lives down the lane

Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full

Отступите от левого края расстояние, равное двум табуляциям. Выполните перенос текста на новую строку двумя способами'''
baby_song = """
\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir,
\t\tThree bags full\n
\t\tOne for the master,
\t\tOne for the dame,
\t\tAnd one for the little boy
\t\tWho lives down the lane

\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir,
\t\tThree bags full."""
print(baby_song)