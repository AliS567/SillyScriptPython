
# Lets ask the user for the inputs

myList = []
N = 2
while len(myList) < N:

    Fname = input("Please enter your forename, and then press Enter:\n")
    Sname = input("Please enter your surname, and then press Enter:\n")
    Height = input("Please enter your height in <ft>, <inches>, and then press Enter:\n")
    Weight = float(input("Please enter your weight in stone, and then press Enter:\n"))
    Age = int(input("Please enter your age, and then press Enter:\n"))

    Feet, inches = str.split(Height)
    Feet = Feet[:-1] # This is just to remove the comma after feet input
    WeightKG = Weight * 6.35
    DoB = 2022 - Age

    x = "Dear {} {}, you are {}, {} ft {} inches, {:.2f} kg and you were born in {}. Notice the bold date {}; this is calculated from the data and you could do this from subtracting the age from the current year which (I think) is 2022.".format(Fname, Sname, Age, Feet, inches, WeightKG, DoB, DoB)
    myList.append([x])


print(myList)