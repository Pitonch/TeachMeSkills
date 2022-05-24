def dic_from_str_letters(input_str: str):
    string_ = list(input_str.replace(' ', ''))
    string_dic = {}.fromkeys(string_, 0)
    for x in string_:
        string_dic[x] += 1
    # print(list(string_dic.values()))
    b = len(str(max(list(string_dic.values()))))
    # print(b)
    if any(col >= 10 for col in (list(string_dic.values()))) is True:
        for k in string_dic:
            print(f'| {k} |{string_dic[k]:<{b}} |')
    else:
        for k in string_dic:
            print(f'| {k} | {string_dic[k]:<{b}} |')


a = input('inset a string: ')
dic_from_str_letters("a")