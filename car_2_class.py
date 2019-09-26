from vehicle_class_2 import *

class Car2(Vehicle2):



    def make_sound(self):
        return 'VROOOOM!'

print('Proof of inheritance')
print(Car2(2, 4, 'Blue', 5))
print(Car2(2, 4, 'Blue', 5).accelerate())

print('Proof of method polymorphisim with make_sound')
print(Vehicle2(2, 4, 'Blue', 6).make_sound())
print(Car2(2, 4, 'Blue', 6).make_sound())