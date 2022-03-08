from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


"""
This has the same output we saw earlier, even though most of the logic
is hidden away in a module.
"""
