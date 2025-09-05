# find the power off any number x ^ y
while True:
    # take input from the user
    x = float(input("Enter the base number (x): ")) # enter the base number
    y = float(input("Enter the exponent (y): ")) # enter the exponent

    # calculate x raised to the power y
    result = round(x ** y, 2) # round the result to 2 decimal places

    # display the result
    print(result)

    # ask user if they want to continue
    choice = input("Do you want to calculate again? (yes/no): ")
    # break the loop if user chooses 'no'
    if choice.lower() == "no": # lower() method is used to convert the string to Lowercase
        print("Thank you for using the Power Calculator!")
        break