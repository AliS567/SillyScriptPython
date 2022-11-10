x1 = 10
x2 = 20
y1 = 15
y2 = 25

# Lets find the Euclidean distance 

Euclidean = ((x1-y1)**2 + (x2-y2)**2)**0.5 

print("The Euclidean distance is: ", Euclidean)

# Lets find the Manhattan distance
from math import abs

Manhattan = abs(x1 - x2) + abs(y1 - y2)
