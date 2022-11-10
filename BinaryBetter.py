# This is a script for lab 2 excercise 1a

x = input("Please provide an 8-bit binary number: \n")

missing = 8 - len(x)

if len(x) < 8:
	print("your number was less than 8-bits!")
	x = "0" * missing + x
	print("It has been augmented to: ", x)
if len(x) > 8:
	print("your number was larger than 8-bits!")
	exit()

number = 0

for i in range(len(x)):
	if x[i] == '1':
		number += 2**i

print("The integer number is: ", number)
