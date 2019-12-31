number = input("Please enter a number: ")
number = int(number)
remainder = number % 10
if(remainder == 0):
    print("That is a base 10 number.")
else:
    print("That is not a base 10 number.")