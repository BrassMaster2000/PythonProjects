#Demo of the print statement

print("\n")
print("Hello World")
print("This is a test of the print statement")
print("\n")

firstName = "David"
lastName = "Weber"

print("Your name is " + firstName + " " + lastName + ".")

print("{0} first name {1} last name".format(firstName, lastName))

firstNumber = 5
secondNumber = 10

print(firstNumber + secondNumber)
print(firstNumber, secondNumber)
print("{0} is greater than {1}".format(secondNumber, firstNumber))

highTestScore = 0.9372
lowTestScore = 0.4598

print("\nThe high score was " + str(highTestScore) + "\nThe low score was " + str(lowTestScore))
print("\nThe high score was {0:.2f} \nThe low score was {1:.2f}".format(highTestScore, lowTestScore))

print("\n\nThe print a list of things\n"
        "Apple\n"
        "Banana\n"
        "Orange\n")