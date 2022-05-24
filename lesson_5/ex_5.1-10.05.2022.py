def pos_neg(input_number: str):
# заменяем , на .
    number = input_number.replace(',', '.')
# проверяем на кол-во точек и дефисов
    if number.count("." and "-") <= 1:
        if "-" or "" in number[0]:
            # заменяем -, . на пустоту и проверяем число ли перед нами
                a = number.replace('-', '')
                if (a.replace('.', '').isdigit()) is True:
                    if float(number) > 0:
                        return 'you entered a positive number'
                    elif float(number) < 0:
                        return 'you entered a negative number'
                    else:
                        return 'you entered zero'
                else:
                    return "you didn't enter a number4"
        else:
            return "you didn't enter a number2"
    else:
        return "you didn't enter a number1 амам"


input_number = input('inset a number: ')
print(pos_neg(input_number))




