import random


N = int(input("Chose an integer for the size of N"))
L = int(N/2)
R = N-L

for i in range(N):
    direction = random.randint(1, 2)
    if R == 0 or L == 0:
        print("We reached the end of the row! Can't take any more steps.")
        break
    elif  direction == 1:
        R += 1
        L -= 1
    elif direction == 2:
        R -= 1
        L += 1
    print("*" * L + "C" + "*" * R)

print("Done")
