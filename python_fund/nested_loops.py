smile = '\U0001f600'
for i in range(10):
    count = 0
    emoticons = ''
    while count <= i:
        emoticons = emoticons + smile
        count = count + 1
    print(f"{emoticons}")

for i in range(1, 11):
    print(smile * i)

for num in range(10):
    emoticons = ''
    for j in range(num + 1):
        emoticons += '\U0001f600'
    print(emoticons)

nested_list = [[1, 2, 3 ], [4, 5, 6], [7, 8, 9], [10, 11, 12],[13, 14, 15, 16], ['hello', 23, True, 'world', 5.2]]
print(nested_list)
print(nested_list[0])
print(nested_list[1])
print(nested_list[-1])
print(nested_list[2][0])
print(nested_list[4][3])

for inner_list in nested_list:
    print(inner_list)

for inner_list in nested_list:
    for num in inner_list:
        print(num)

[[print(num) for num in inner_list] for inner_list in nested_list]