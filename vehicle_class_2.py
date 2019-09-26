class Vehicle2 ():

    def __init__(self, wheels, capacity, colour, year):
        self.wheels = wheels
        self.capacity = capacity
        self.colour = colour
        self.year = year

    def accelerate(self):
        return 'Vrooooom'

    def make_sound(self):
        return '##Making Noooises'

print(Vehicle2(4, 5, 'Green', 1967))