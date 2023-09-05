# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# class TownCar:
#     speed = 80
#     color = "Зеленый"
#     name = "Москвич"
#     is_police = 161616681861616513314545
#
#     def goo(self, speed, color, name, is_police):
#         print("Машина поехала")
#
#     def stop(self):
#         print("Машина остановилась")
#
#     def tern_r(self):
#         print("Машина повернула направо")
#
#     def tern_l(self):
#         print("Машина повернула налево")
#
# a = TownCar()
# print(a.color, a.name, "вы двигаетесь со скоростью:", a.speed, "км/ч", "Ваш VIN: ", a.is_police)
# # a.goo()
# # a.stop()
# a.tern_r()
#
# class SportCar(TownCar):
#     speed = 190
#     color = "Красный"
#     name = "Ferarry"
#     is_police = 16155848861616513314545
#
# a = SportCar()
# print(a.color, a.name, "вы двигаетесь со скоростью:", a.speed,"км/ч", "Ваш VIN: ", a.is_police)
# a.tern_l()
#
# class WorkCar(TownCar):
#     speed = 190
#     color = "Белый"
#     name = "Камаз"
#     is_police = 1615516514661616513314545
#
# a = WorkCar()
# print(a.color, a.name, "вы двигаетесь со скоростью:", a.speed,"км/ч", "Ваш VIN: ", a.is_police)
# a.tern_l()
#
# class PoliceCar(TownCar):
#     speed = 140
#     color = "Синий"
#     name = "Hyndai"
#     is_police = 16155848861616513314545
#
# a = PoliceCar()
# print(a.color, a.name, "вы двигаетесь со скоростью:", a.speed,"км/ч", "Ваш VIN: ", a.is_police)
# a.tern_r()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"Автомобиль {self.name}, {self.color} цвет поехал со скоростью {self.speed} км/ч")

    def stop(self):
        print(f"Автомобиль {self.name}, {self.color} цвет остановился")

    def tern_l(self):
        print(f"Автомобиль {self.name}, {self.color} цвет повернул налево")

    def tern_r(self):
        print(f"Автомобиль {self.name}, {self.color} цвет повернул направо")

a = TownCar(100, "зеленый", "Москвич")
a.go()
a.stop()
a.tern_r()
a.tern_l()

class SportCar(TownCar):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

a = SportCar(200, "красный", "Ferarry")
a.go()
a.stop()
a.tern_r()
a.tern_l()

class WorkCar(TownCar):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

a = WorkCar(80, "белый", "Камаз")
a.go()
a.stop()
a.tern_r()
a.tern_l()

class PoliceCar(TownCar):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

a = PoliceCar(140, "синий", "Hyndai")
a.go()
a.stop()
a.tern_r()
a.tern_l()