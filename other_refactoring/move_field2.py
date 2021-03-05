# Kami Bigdely
# Move Field


class Car:
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)

        self.cabin = cabin
        self.fuel_tank = fuel_tank


class Tpms:
    """Tire Pressure Monitoring System."""

    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300  # [feet]
        self.sensor_pressure_range = (8, 300)  # [PSI]
        self.battery_life = 6  # [year]

    def get_pressure(self):
        return 3

    def get_serial_number(self):
        return self.serial_number


class Wheel:
    def __init__(self, serial_number, wheel_location=None, car=None):
        self.tpms = Tpms(serial_number)
        self.car = car
        self.wheel_location = wheel_location

    def install_tire(self):
        print("remove old tube.")
        print(
            "cleaned tpms: ",
            self.car.tpms_di[self.wheel_location].get_serial_number,
            ".",
        )
        print("installed new tube.")

    def get_serial_number(self):
        return self.tpms.get_serial_number()

    def get_location(self):
        return self.wheel_location

    def read_tire_pressure(self):
        return self.tpms.get_pressure()

    def set_car(self, car):
        self.car = car


class Engine:
    def __init__(self):
        pass


class FuelTank:
    def __init__(self):
        pass


class Cabin:
    def __init__(self):
        pass


engine = Engine()
wheels = [
    Wheel(983408543, "front-right", None),
    Wheel(4343083, "front-left", None),
    Wheel(23654835, "back-right", None),
    Wheel(3498857, "back-left", None),
]

cabin = Cabin()


fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)
