# Let's import all the relevant libraries
import numpy as np
import matplotlib.pyplot as plt
import random

# Lets get the grid size from the user
n = input("Please enter grid size. ")

# Let's make lists for the positions Note: here i make x, y lists and pos.
x = [0]
y = [0]
pos = [[0,0]]

# Let's set up the variables for the grid hashtags
L = int(n/2)
R = int(n/2)
U = int(n/2)
D = int(n/2)

# Define our movement choices, to be selected randomly
directions = ["UP", "DOWN", "LEFT", "RIGHT"]

# Let's print the grid initially
for j in range(U):
    print((L*"#"+"#"+"#"*R))
print(L*"#"+"O"+"#"*R)
for j in range(D):
    print((L*"#"+"#"+"#"*R))
print()

# Lets run our experiments
for i in range(1, n):
    
    # Pick a direction at random
    step = random.choice(directions)
    
    # Move the object according to the direction
    # Note we alter L,R,U,D based on our choice
    # We also update the objects positions and append
    # to the positions lists
    if step == "RIGHT":
        L += 1
        R -= 1
        pos.append([pos[i-1][0] + 1, pos[i-1][1]])
        x.append(x[i - 1] + 1)
        y.append(y[i - 1])
    elif step == "LEFT":
        L -= 1
        R += 1
        pos.append([pos[i-1][0] - 1, pos[i-1][1]])
        x.append(x[i - 1] - 1)
        y.append(y[i - 1])
    elif step == "UP":
        D += 1
        U -= 1
        pos.append([pos[i-1][0], pos[i-1][1] + 1])
        x.append(x[i - 1])
        y.append(y[i - 1] + 1)
    elif step == "DOWN":
        D -= 1
        U += 1
        pos.append([pos[i-1][0], pos[i-1][1] - 1])
        x.append(x[i - 1])
        y.append(y[i - 1] - 1)

    # Print our grid with the objects movement
    for j in range(U):
        print((L*"#"+"#"+"#"*R))

    print(L*"#"+"O"+"#"*R)

    for j in range(D):
        print((L*"#"+"#"+"#"*R))

    print()

# Print the list of objects positions
print(pos)
