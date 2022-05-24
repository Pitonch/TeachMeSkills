# list(input('inset a string: ').replace(' ', ''))
string_ = list(input('inset a string: ').replace(' ', ''))
string_dic = {}.fromkeys(string_, 0)
for x in string_:
    string_dic[x] += 1
# print(list(string_dic.values()))
b = len(str(max(list(string_dic.values()))))
# print(b)
if any(a >= 10 for a in (list(string_dic.values()))) is True:
    for k in string_dic:
        print(f'| {k} |{string_dic[k]:<{b}} |')
else:
    for k in string_dic:
        print(f'| {k} | {string_dic[k]:<{b}} |')

