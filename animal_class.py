# Define animal class

class Animal():
    # Class is a cookie cutter for objects:
        # Wraps its characteristics and behaviours
    # Have some characteristics
        # Default values are the end argument
    def __init__(self, name, eyes, legs, age = 0):
        self.name = name
        self.bones = True
        self.alive = True
        self.number_eyes = eyes
        self.number_legs = legs
        self.age = age

    # Define some behaviours - Methods
        # Things an instance of an object can do
        # Functions that are dependent on an object type

    def eat(self, food):
        return 'NOM NOM NOM!' + food

    def mating(self):
        return ' <3 '

    def mate_calling(self):
        return 'Swipe right ;)'

    def sleep(self):
        return 'zzzzzz'

    def go_potty(self):
        return 'HHUMMMM!! .... 0.0 ! -.-   -- zen'



