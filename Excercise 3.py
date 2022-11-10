# This is the script solution for lab 2 excercise 3

length = 12

for i in range(length):
    for j in range(length):
        if(i == 0 or i not in range(int((length/2)-3),int((length/2)+3))  or j == 0 or j not in range(int((length/2)-3),int((length/2)+3))):
            print('#', end = ' ')
        else:
            print(' ', end = ' ')
    print()