ageask = "\nHow old are you? "
ageask += '\nEnter quit to stop: '

MovieGoerNumber = 1

while MovieGoerNumber == 1:
    age = input(ageask)

    if age != 'quit':

        age = int(age)
    
        if age < 3:
            print("The ticket is free.")
        elif age < 12:
            print("The ticket is $10.00")
        elif age > 12:
            print("The ticket is $15.00")
    
    if age == 'quit':
        MovieGoerNumber = 0
