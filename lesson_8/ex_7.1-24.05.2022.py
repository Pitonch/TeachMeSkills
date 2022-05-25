import time


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


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='black', weight=1700, ):
        self.max_load = max_load
        Auto.__init__(self, brand, age, mark, color='black', weight=1700)

    def move(self):
        print('attention move')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='black', weight=1700, ):
        self.max_speed = max_speed
        Auto.__init__(self, brand, age, mark, color='black', weight=1700)

    def move(self):
        print('attention move')
        print('max speed is ' + str(self.max_speed))


skoda_car = Auto(brand='Skoda', age=3, color='red', mark='rapid', weight=1700)
opel_car = Auto('Opel', 99, 'black', 'Vectra', 2500)
track_daf = Truck('DAF', 25, 'sn1236', 3700)
track_volvo = Truck('Volvo', 0, 's905', 5000)
car_1 = Car('mersedes', 1, 's40', 250)
car_2 = Car('mazda', 5, 'xerox', 140)


print(skoda_car.color)
print(opel_car.weight)
skoda_car.move()
print(skoda_car.birthday())
print(opel_car.birthday())

track_daf.move()
track_daf.load()

car_1.move()
car_2.move()