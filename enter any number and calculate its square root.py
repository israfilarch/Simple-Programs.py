# Calculate the square root of a positive number entered by the user

while True: # Loop until a valid number is entered

    # input any number from the user
    number = float(input("Enter any positive number to calculate square root: "))

    # check if the number is negative
    if number < 0:
        print("Please enter a non-negative number.") # prompt the user to enter a valid number
        continue
    
    # Calculate the square root
    root = round(number ** 0.5, 2) # rounding to 2 decimal places 
    
    # print the result
    print("The square root of", number, "is", root)

    # ask the user if they want to continue
    choice = input("Do you want to calculate another square root? (yes/no): ")

    # if the user does not want to continue, break the loop
    if choice.lower() != 'yes': # lowercase to handle case insensitivity
        break