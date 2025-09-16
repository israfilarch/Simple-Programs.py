# read the temperature state and show massege if the temperature is too high or too low

while True: # infinite loop for continuous input

    # take input from user
    temp = float(input("Enter the temperature in Celsius: "))

    if temp <= 0:
        print(temp,"This is Freezing temperature") # less than or equal to 0 show this result

    elif temp > 0 and temp < 10: 
        print(temp,"This is Very Cold weather")  # less than 10 and greater than 0 show this result

    elif temp >= 10 and temp < 20:
        print(temp,"This is Cold weather") # less than 20 and greater than or equal to 10 show this result

    elif temp >= 20 and temp < 30:
        print(temp,"This is Normal in Temp") # less than 30 and greater than or equal to 20 show this result
    
    elif temp >= 30 and temp < 40:
        print(temp,"This is Hot weather") # less than 40 and greater than or equal to 30 show this result

    elif temp >= 40:
        print(temp,"This is Very Hot weather") # greater than or equal to 40 show this result

    else: 
        print("Invalid input") # if the input is not a number show this result

        # ask to continue or not
        cont = input("Do you want to continue? (yes/no): ").lower()

        if cont != 'yes': # if the user does not want to continue,

            break # break the loop and end the program