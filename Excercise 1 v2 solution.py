# Let's get the grid size and number of runs form the user
N = int(input("Please enter a grid size. "))

# Let's set up the 2D grid
grid = []
for i in range(N):
    grid.append(["~"]*N)

# Set the initial character to "O"
grid[int(N/2)][int(N/2)] = 'X'

# Import the random library so we can get a random choice on each iteration
import random

# Define our choices
choices = ["R", "L", "U", "D"]

# Set the original position to a list so we can append new positions to it
pos = [[int(N/2), int(N/2)]]

# Run through experiments for random choices, appending each new position to position list
for i in range(1,N):
    x = random.choice(choices)
    if x == "R":
        pos.append([pos[i-1][0]+1, pos[i-1][1]])
    elif x == "L":
        pos.append([pos[i-1][0]-1, pos[i-1][1]])
    elif x == "D":
        pos.append([pos[i-1][0]  , pos[i-1][1]+1])
    elif x == "U":
        pos.append([pos[i-1][0]  , pos[i-1][1]-1])

# Run the experiments for the amount of times we had position changes,
# update the special character location based on each position in the
# position list NOTE: the first run runs for position [0, 0]
for k in range(len(pos)):
    grid = []
    for i in range(N):
        grid.append(["~"]*N)

    grid[pos[k][0]][pos[k][1]] = 'X'
    for i in range(len(grid)):
        print(grid[i])
    print("\n")
