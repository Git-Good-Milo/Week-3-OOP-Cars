class Vehicle():

    def __init__(self, type, num_of_wheels, num_of_seats, colour, date_of_manufacture):
         self.vehicle_type = type
         self.wheels = int(num_of_wheels)
         self.capacity = int(num_of_seats)
         self.vehicle_colour = colour
         self.year = (date_of_manufacture)


    def accelerate(self, rate_of_speed ):
        return rate_of_speed + '. Damn this thing is can move!'

    def brake(self, speed_till_0):
        return speed_till_0 + '. My face has ripped off!'

    def turn(self, angle_of_turn):
        return angle_of_turn
