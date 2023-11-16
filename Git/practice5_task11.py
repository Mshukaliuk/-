class Vehicle(object):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def honk(self, work:bool = False):
        if work == True:
            print("Beep!")

class LandVehicl(Vehicle):
    def __init__(self, make, model, speed: int = 0): #якщо є додаткові параметри
        super().__init__(make, model)
        self.speed = speed

    def drive(self, speed_increase: int):
        self.speed = self.speed + speed_increase
        if self.speed > 0: print('Їдемо по суші')
        elif self.speed == 0: print('Ми стоїмо')


# Car: Наслідується від LandVehicle.
# Унікальний метод: open_trunk(), який виводить "Багажник відкрито".

class CarClassC(LandVehicl):
    def __init__(self, make, model,speed):
        self.make = make
        self.model = model
        self.speed = speed

    def open_car(self):
        print("Багажник відкрито")


# Truck: Наслідується від LandVehicle.
# Унікальний метод: load_cargo(), який виводить "Вантаж завантажено".


# Підкласи від WaterVehicle:
# Boat: Наслідується від WaterVehicle.
# Унікальний метод: anchor(), який виводить "Човен на якорі".
#
# Ship: Наслідується від WaterVehicle.
# Унікальний метод: sound_horn(), який виводить "Гудок корабля".

    if __name__ == '__main__': # Code to execute

            car1 = LandVehicl('Toyota', 'Camry')
            car1.drive(10)

            car2 = CarClassC('Toyota', 'Camry')
            car2.open_car()
