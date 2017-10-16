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
#this will assign the above to a variable that can be easily used in the rest of the code
var = (random.choice(Trek))
#however, this will establish var as the same choice every time. The variable needs to be deleted each time the script is run:
del var
var = (random.choice(Trek))
if var == TOS:
  y = (randint(1,3))
  print (var, y)
else:
  y = (randint(1,7))
  print (var, y)
del var
del y
