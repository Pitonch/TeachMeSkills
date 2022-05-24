input_number = input('inset a number: ')
# заменяем , на .
number = input_number.replace(',', '.')
# проверяем на кол-во точек и дефисов
if number.count("." and "-") <= 1:
    if "-" or "" in number[0]:
        # заменяем -, . на пустоту и проверяем число ли перед нами
            a = number.replace('-', '')
            if (a.replace('.', '').isdigit()) is True:
                if float(number) > 0:
                    print('you entered a positive number')
                elif float(number) < 0:
                    print('you entered a negative number')
                else:
                    print('you entered zero')
            else:
                print("you didn't enter a number4")
    else:
        print("you didn't enter a number2")
else:
    print("you didn't enter a number1")




