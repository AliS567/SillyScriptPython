# This version of the solution counts clusters of 0's and 1's
import random
import re

# Lets ask the user for a string size
N = int(input("insert the size of string you want"))

# Initialise the string so we can append random values
_string = ""

# Append random values for the users length selection
for l in range(N):
	_string += str(random.randint(0,1))

# Print the string so we can see what is created
print(_string)

# Do a quick check that the user string is longer than 1
if _string == len(_string) * _string[0]:
    print(f"Your cluster size is: {len(_string)} and there's 1")
    exit()

# Lets account for string wrapping, this checks if the last
# digit is the same as the starting one and alters the string
# to wrap around until that is not the case anymore
if _string[0] == _string[-1]:
    n_string = ''
    print("We need to do some string alterations, to account for wrapping")
    for i in range(1, len(_string)):
        if _string[-(i)] == _string[0]:
            n_string += _string[-(i)]
        else:
            n_string += _string[:-(i)+1]
            break
    print("your new string is: {}".format(n_string))
    _string = n_string

# The line below finds all the clusters in the string
LC = [m.group(0) for m in re.finditer(r"(\d)\1*", _string)]

# count size of each cluster and add them all together
size = 0
for i in LC:
    size += len(i)

# Find the average, number of clusters and print to screen
print("average cluster size: {}".format(size/len(LC)))
print("there are {} clusters".format(len(LC)))