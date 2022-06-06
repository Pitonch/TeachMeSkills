import math
import re

# находим в строке оператор, который указывает на действие для выполнения, можно дополнять
def input_(a):
    if '+' in a:
        return '+'
    if '-' in a:
        return '-'
    if '*' in a:
        return '*'
    if '/' in a:
        return '/'
    if '^' in a:
        return '^'


# по оператору находим функцию которую нужно подключить в калькулятор
def sum_():
    i = insert_num.index('+')
    a = insert_num[:i]
    b = insert_num[i+1:]
    return float(a) + float(b)


def minus_():
    i = insert_num.index('-')
    a = insert_num[:i]
    b = insert_num[i+1:]
    return float(a) - float(b)


def division_():
    i = insert_num.index('/')
    a = insert_num[:i]
    b = insert_num[i+1:]
    return float(a) / float(b)


def multiplication_():
    i = insert_num.index('*')
    a = insert_num[:i]
    b = insert_num[i+1:]
    return float(a) * float(b)


insert_num = input("Введите выражение из двух значений: ").replace(' ', '')
x = re.fullmatch(r'^\d+[*-/+]\d+$', insert_num)
if x is None:
    print('вы ввели не верные данные')
else:
    if input_(insert_num) == '+':
        print(sum_())

    if input_(insert_num) == '-':
        print(minus_())

    if input_(insert_num) == '/':
        print(division_())

    if input_(insert_num) == '*':
        print(multiplication_())
