# def int_in_str(a: int):
#     return str(a)

# def odd(a):
#     if a%2 == 0:
#         return 'четное'
#     else:
#         return 'не четное'
# print(odd(5))


b = lambda a: 'четное' if a % 2 == 0 else 'не четное'
print(b(-5))


number_list = [1, 2, 3, 4]
print(list(map(lambda a: str(a), number_list)))


def polydrom_(a: tuple):
    a_revers = a[::-1]
    if a == a_revers:
        return True


word_tuple = ('мам', 'папа', 'малина', 'оро')
print(tuple(filter(polydrom_, word_tuple)))

print(tuple(filter(lambda x: x == x[::-1], word_tuple)))




