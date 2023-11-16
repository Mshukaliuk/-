class Vehicle(object):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def honk(self, work:bool = False):
        if work == True:
            print("Beep!")

class LandVehicl(Vehicle):
    def __init__(self, make, model, speed:int = 0):
        super().__init__(make, model)
        self.speed = speed

    def drive(self, speed_increase: int):
        self.speed = self.speed + speed_increase
        if self.speed > 0: print('Їдемо по суші')
        elif self.speed == 0: print('Ми стоїмо')

car = LandVehicl('Toyota','Camry')
car.drive(10)

class WaterVehicle(Vehicle):
    def __init__(self, make, model, speed:int = 0):
        super().__init__(make, model)
        self.speed = speed

    def drive(self, speed_increase: int):
        self.speed = self.speed + speed_increase
        if self.speed > 0: print('Їдемо по суші')
        elif self.speed == 0: print('Ми стоїмо')

boat = LandVehicl('BoatBrand','BoatModel')
boat.drive(10)

# Car: Наслідується від LandVehicle.
# Унікальний метод: open_trunk(), який виводить "Багажник відкрито".

class Car(LandVehicl):

    def open(self):
        print("Багажник відкрито")

# Truck: Наслідується від LandVehicle.
# Унікальний метод: load_cargo(), який виводить "Вантаж завантажено".

car.open()

# Підкласи від WaterVehicle:
# Boat: Наслідується від WaterVehicle.
# Унікальний метод: anchor(), який виводить "Човен на якорі".
#
# Ship: Наслідується від WaterVehicle.
# Унікальний метод: sound_horn(), який виводить "Гудок корабля".