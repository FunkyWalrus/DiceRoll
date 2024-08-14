from random import randint

rollAgain = True

def getNumberOfDice():
    try:
        numberOfDice = int(input("Please enter how many dice to roll: "))
        return numberOfDice
    except ValueError:
        print("You did not enter a valid integer.")
        getNumberOfDice()

def getNumberOfDiceFaces():
    try:
        numberOfDiceFaces = int(input("Please enter how many faces each die should have: "))
        return numberOfDiceFaces
    except ValueError:
        print("You did not enter a valid integer.")
        getNumberOfDiceFaces()

while rollAgain:
    numberOfDice = 0
    numberOfDiceFaces = 0

    totalRollValue = 0
    totalRollString = ""
    
    numberOfDice = getNumberOfDice()
    numberOfDiceFaces = getNumberOfDiceFaces()
    
    for i in range(numberOfDice):
        currentRollValue = randint(1,numberOfDiceFaces)
        totalRollString += str(currentRollValue)
        totalRollString += ", "
        totalRollValue += currentRollValue
    print(totalRollString)
    print("You rolled a total of:", totalRollValue, ", in", numberOfDice, "dice rolls with", numberOfDiceFaces, "faces each.")
    print("Do you want to roll again? Enter y or yes to continue.")
    rollAgain = ("y" or "yes") in input().lower()



print("You didn't enter y or yes, so the program will now end.")