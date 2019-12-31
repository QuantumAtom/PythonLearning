from car import Car
from electric_car import ElectricCar

my_new_car = car.Car('audi', 'a4', 2016)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_beetle = car.Car('chevy', 'malibu', 2012)

print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)

print(my_tesla.get_descriptive_name())

