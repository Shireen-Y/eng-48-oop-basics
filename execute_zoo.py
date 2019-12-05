from animal_class import *
from reptile_class import *

# Create 2 reptiles

reptile1 = Reptile('Ringo', 2, 4, 17)
reptile2 = Reptile('Susan', 2, 4, 16)

# Make the reptiles sleep
print(reptile1.sleep())
print(reptile2.sleep())
print(reptile1.mate_calling())
print(reptile1.n_chamber_heart)