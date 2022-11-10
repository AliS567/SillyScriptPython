
# Lets ask the user for the inputs

myList = []
N = 1
while len(myList) < N:

    Fname = input("Please enter your forename, and then press Enter:\n")
    Sname = input("Please enter your surname, and then press Enter:\n")
    Height = input("Please enter your height in <ft>, <inches>, and then press Enter:\n")
    Weight = float(input("Please enter your weight in stone, and then press Enter:\n"))
    Age = int(input("Please enter your age, and then press Enter:\n"))

    myList.append([Fname, Sname, Height, Weight, Age])

# Let allow the user to chose a row to print

row = int(input("Please enter a row to address, any number from 0 to {}:\n".format((N-1))))

print(myList[row])

col = int(input("Please select a column to address,, any number from 0 to {}:\n".format((len(myList[0])))))

print(myList[row][col])
