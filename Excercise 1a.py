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

if x[0] == '1':
	number += 128
if x[1] == '1':
	number += 64
if x[2] == '1':
	number += 32
if x[3] == '1':
	number += 16
if x[4] == '1':
	number += 8
if x[5] == '1':
	number += 4
if x[6] == '1':
	number += 2
if x[7] == '1':
	number += 1

print("The integer number is: ", number)
