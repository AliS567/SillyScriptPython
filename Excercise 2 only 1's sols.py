# This solution only counts the number of clusters of 1's
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

# Let's split the string based on 0's NOTE: this returns some empty strings 
clus = _string.split('0')
# Let's remove the empty strings, this method uses 'list comprehension'
clus = [x for x in clus if x != '']
# You can also use for loops and filter to do the above!
print(clus)
# Now print the average cluster size to the screen, number of clusters can 
# be found by using the len() function on the cluster list, but we also need
# to find the size of each cluster string in the list

# First lets find the size of each string element in the list
size = 0
for i in clus:
    size += len(i)


print(f"The average cluster size is: {size/len(clus)}")
print("The number of clusters in the string is: {}".format(len(clus)))