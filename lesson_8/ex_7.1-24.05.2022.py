class Auto:

# задаем атрибуты
    def __init__(self, brand, age, mark, color='black', weight=1700):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

# пишем метод (это функция находящаяся внутри класса)
    def move(self):
        print('move')

    def birthday(self):
        self.age += 1
        return self.age

    def stop(self):
        print('stop')


skoda_car = Auto(brand='Skoda', age=3, color='red', mark='rapid', weight=1700)
opel_car = Auto('Opel', 99, 'black', 'Vectra', 2500)


print(skoda_car.color)
print(opel_car.weight)

skoda_car.move()
print(skoda_car.birthday())
print(opel_car.birthday())