from vehicle_class import *
from car_class import *
from bike_class import *

my_favourite_vehicle = Vehicle('Car', 4, 4, 'Blue', 2019)

my_favourite_car = Car('Supra', 4, 4,'blue', 1997, 'Toyota', 'MKIV','Ad54A', 2)

print(my_favourite_car.accelerate('60kph'))
print(my_favourite_car.security('Lock and chain'))
print(my_favourite_vehicle.accelerate('60kph'))

# self, num_of_wheels, num_of_seats, colour, date_of_manufacture, make, model_num, license_num, num_of_air_bags