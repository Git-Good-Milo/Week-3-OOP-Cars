from vehicle_class import *

class Car(Vehicle):
# Characteristics
    def __init__(self, type,  num_of_wheels, num_of_seats, colour, date_of_manufacture, make, model_num, license_num, num_of_air_bags):
        super().__init__(type, num_of_wheels, num_of_seats, colour, date_of_manufacture)
        self.brand = make
        self.model = model_num
        self.license_plate = license_num
        self.saftey = int(num_of_air_bags)


        # Behaviours

    def play_music(self, genre):
        return 'I love this song! Whats the genre? ' + genre

    def horn(self, horn_sound):
        return horn_sound

    def security(self, lock_it = 'Imobiliser'):
        return 'Car uses: ' + lock_it

    def accelerate(self, rate_of_speed ):
        return rate_of_speed + '. Damn this thing super slow!'