# Lets import the random library so that we 
# can have random selections
import random

# Ask the user for however many runs is needed
M = int(input("How many runs? "))

# Set values for hashtags on the left and right
L = int( M/2 )
R = int( M/2 )

# Initialize list for storing probability of
# heads per run, along with integer count for
# amount of times heads has appeared 
prob_list = []
num_H = 0

# Print the first frame of the graphic
print("#" * L + "C" + "#" * R)

# Run for the specified run lengths
for i in range(M):
    
    # Chose the random integer of 1 (heads)
    # or 2 (tails)
    x = random.randint(1, 2)

    # Check if we ran out of places for #'s
    if L == 0 or R == 0:
        print("WE RAN OUT OF SPACE")
        break
    # If heads change values for graphic and
    # add 1 to the number of heads variable
    elif x == 1:
        L -= 1
        R += 1
        num_H += 1
    # If tails change values for graphic
    else:
        L += 1
        R -= 1
    # Append the number of heads/runs to list
    # after each run (or experiment)
    prob_list.append(num_H/(i+1))
    
    # Print the graphic with the updated sides
    print("#" * L + "C" + "#" * R)

# Print the heads probabilities list
print(prob_list)