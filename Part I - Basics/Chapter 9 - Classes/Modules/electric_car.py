from car_v2 import Car


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This can can go approximately " + str(range)
        message += " miles on a  full charge."
        print(message)


class ElectricCar(Car):
    """Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
