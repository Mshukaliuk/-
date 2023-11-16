class Vehicle(object):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def honk(self, work: bool = False):
        if work == True:
            print("Beep!")

"""
Parent class for all Vehicles (Class A).

    Parameters
    ----------
    make: str
        Vehicle producer
    model: str
        Vehicle model

    Returns
    -------
    str
        If it works (bool == 1) - it makes "Beep!" sound.
"""

class LandVehicl(Vehicle):
    def __init__(self, make, model, speed: int = 0):  # якщо є додаткові параметри
        super().__init__(make, model)
        self.speed = speed

    def drive(self, speed_increase: int):
        self.speed = self.speed + speed_increase
        if self.speed > 0:
            print('Їдемо по суші')
        elif self.speed == 0:
            print('Ми стоїмо')
        else:
            print('Швидкість не може бути < 0')

"""
Child class for LandVehicl (Class B), which is following Vehicles (Class A).
"""

class CarClassC(LandVehicl):
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    def open_car(self):
        print("Багажник відкрито")

"""
Child class for CarClassC (Class C), which is following LandVehicle (Class B).
"""

class TruckClassC(LandVehicl):
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    def load_cargo(self):
        print("Вантаж завантажено")


"""
Child class for TruckClassC (Class C), which is following LandVehicle (Class B).
"""

class WaterVehicle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)


class BoatClassC(WaterVehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def anchor(self):
        print("Човен на якорі")

"""
Child class for WaterVehicle (Class B), which is following Vehicles (Class A).
"""

class ShipClassC(WaterVehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def sound_horn(self):
        print("Гудок корабля")

"""
Child class for ShipClassC (Class C), which is following WaterVehicle (Class B).
"""

#########################################################################################################################

if __name__ == '__main__':  # Code to execute

    car1 = LandVehicl('Toyota', 'Camry')
    car1.honk(True)
    car1.drive(0)
    car1.drive(10)
    car1.drive(-11)

    car2 = CarClassC('Toyota', 'Camry', 0)
    car2.open_car()

    car3 = TruckClassC('Toyota', 'Camry', 50)
    car3.load_cargo()

    boat1 = BoatClassC('Toyota', 'Camry')
    boat1.anchor()

    ship1 = ShipClassC('Toyota', 'Camry')
    ship1.sound_horn()
