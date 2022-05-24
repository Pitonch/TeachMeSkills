import json
import csv


# print('1', "-"*100)
# a = b'r\xc3\xa9sum\xc3\xa9'
# c = a.decode()
# b = c.encode(encoding='Latin1')
# d = b.decode(encoding='Latin1')
#
# print(c)
# print(b)
# print(d)
#
# print('2', "-"*100)
#
# first_str = input('inset 1 string: ')
# second_str = input('inset 2 string: ')
# third_str = input('inset 3 string: ')
# fourth_str = input('inset 4 string: ')
#
# with open('ex 7.1 7.2 7.3 7.4 - 18.05.2022_txt.txt', 'w+') as f:
#     f.write(first_str + '\n')
#     f.write(second_str + '\n')
#
# with open('ex 7.1 7.2 7.3 7.4 - 18.05.2022_txt.txt', 'a+') as f:
#     f.write(third_str + '\n')
#     f.write(fourth_str)

# print('3', "-"*100)
#
# id_ = 123456
# name = 'Jon'
# age = 25
#
#
dic_id = {
    1: ('Jon', 25),
    2: ('Ann', 32),
    3: ('Ol', 90),
    4: ('Dic', 15),
    5: ('Monel', 7),
    6: ('Ron', 56)
}

with open('ex 7.1 7.2 7.3 7.4 - 18.05.2022_json.json', 'w') as f:
    a = f.write((json.dumps(dic_id)))


print('4', "-"*100)

with open('ex 7.1 7.2 7.3 7.4 - 18.05.2022_json.json', 'r') as f:
    data = json.load(f)
    print(data)
for id in data:
    data[id].append(id*3)  # Добавляем номер телефона, как произведение индекса и числа

# А потом нужно добавить и ключ и значение, как список, чтобы записать в файл
# С помощью этого цикла мы сразу же обращаемся и к ключу, и к значению
#  for key, value in data.items():
#         writer.writerow([key, *value])
# Затем используем *value, чтобы распаковать значения и добавить их в новый список [key, *value]


with open('ex 7.1 7.2 7.3 7.4 - 18.05.2022_csv', 'w+') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(('id', 'name', 'age', 'phone'))
    for key, value in data.items():
        writer.writerow([key, *value])
        pass
