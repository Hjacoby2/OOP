import random

class Insect:
    def __init__(self, w, l, n):  # Added 'n' to the parameter list
        self.wings = w  # Insect has 2 wings
        self.legs = l    # Insect has 4 legs
        self.name = n
        self.flight = 0  # To store the random length of flight

    def calc_flight(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight
    
    def get_name(self):
        return self.name
