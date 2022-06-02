import math


def sum_(a:float, b:float):
    return float(a)+float(b)


def minus_(a:float, b:float):
    return float(a)-float(b)


def division_(a:float, b:float):
    return float(a)/float(b)


def multiplication_(a:float, b:float):
    return float(a)*float(b)


def input_num():
    return input('input number: ')



start = input("what kind of mathematical calculation will we do: "
              "\n 'Sum' \n 'Minus' \n 'Division' \n 'MUltiplication' "
              ": ").lower()

if start == 's':
    a = input_num()
    b = input_num()
    print(sum_(a, b))


if start == 'm':
    a = input_num()
    b = input_num()
    print(minus_(a, b))


if start == 'd':
    a = input_num()
    b = input_num()
    print(division_(a, b))

if start == 'mu':
    a = input_num()
    b = input_num()
    print(multiplication_(a, b))
