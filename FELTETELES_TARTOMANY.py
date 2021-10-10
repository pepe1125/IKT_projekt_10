print ("Enter a number between 1 and 10: ")
number = int(input("> "))

if number in range(1, 6):
    print ("You entered a number in the range of 1 to 5")
elif number in range(6, 11):
    print ("You entered a number in the range of 6 to 10")
else:
    print ("Your number wasn't in the correct range")
