#This will select a random series of numbers, representing the Series, Season, and Episode of that season.
from random import randint
x = (randint(1,4))
y = (randint(1,7))
z = (randint(1,24))
print (x, y, z)
#This will select a random series to watch.
import random
Trek = ['TOS', 'TNG', 'DS9', 'VOY', 'ENT']
print (random.choice(Trek))
#This will select a series, then the season (1-7) then the episode (1-24)
print (random.choice(Trek), y, z)
