from vehicle_class import *

class Bike(Vehicle):

    # Charateristscs
    def __init__(self, num_of_wheels, num_of_seats, colour, date_of_manufacture, num_of_gears, handle_type, basket):
        super.__init__(num_of_wheels, num_of_seats, colour, date_of_manufacture)
        self.gears = num_of_gears
        self.handle = handle_type
        self.luggage = basket

    def peddle(self, peddle_shape = 'square'):
        return peddle_shape

    def stunts(self, skills = 'Wheelie'):
        return 'Coh blimey! Was that a ' + skills + '?'

    def security(self, lock_it = 'lock and chain'):
        return lock_it