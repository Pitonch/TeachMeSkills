#одинаковые данные одинаковые идентификаторы
#кортеж
a = (1, 2)
b = (1, 2)
c = (1, 2)
print('кортеж', id(a), id(b), id(c))
print(type(a))

#одинаковые данные разные идентификаторы
#список
a = [1, 2]
b = [1, 2]
print('список', id(a), id(b))
print(type(a))

#словарь
a = {'1': '2', '3': '4'}
b = {'1': '2', '3': '4'}
print('словарь', id(a), id(b))
print(type(a))

#одинаковые данные разные идентификаторы
#кортеж
a = str((1, 2))
b = str((1, 2))
c = str((1, 2))
print('кортеж', id(a), id(b), id(c))
print(type(a))

#одинаковые данные одинаковые идентификаторы
#список
a = [1, 2]
b = [1, 2]
a=b
print('список', id(a), id(b))
print(type(a))










# a = {'1': '2', '3': '4'}
# b = {'1': '2', '3': '4'}
# print(id(a), id(b))
#
# a = str((1, 2))
# b = str((1, 2))
# c = str((1, 2))
# print(id(a), id(b), id(c))
#
# a = str({'1': '2', '3': '4'})
# b = str({'1': '2', '3': '4'})
# print(id(a), id(b))
#








# a = 1
# b = '1'
#
# print(id(a)-id(b))
#
# a = 1
# b = '1'
# c = float(1)
#
#
# print(id(a)-id(b)-id(c))
#
# a = 1
# b = 1
#
# print(id(a), id(b))
#
# а = [1, 2]
# b = [1, 2]
#
# print(id(a), id(b))