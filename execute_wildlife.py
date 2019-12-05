from animal_class import *
from reptile_class import *
# How to create an object
# Creating an instance of animal class
simba = Animal(3, 1, 8)

# Creating a reptile
ringo = Reptile('Ringo', 3, 1, 8)

# Checking data type
# print(simba)
# print(type(simba))

# # Calling methods on an object
# print(simba.eat())
# print(simba.go_potty())
# print(simba.sleep())

# # Calling the attributes of an object
# print(simba.age)
# print(simba.bones)
# print(simba.number_legs)

# Reptile
print(ringo.eat('food'))
print(ringo.seek_heat())

# Animal class doesn't have seek_heat
print(simba.mate_calling())
print(ringo.mate_calling())