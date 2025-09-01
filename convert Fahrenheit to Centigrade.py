# Program to convert Fahrenheit to Centigrade (Celsius)

while True:
    # Take temperature input in Fahrenheit from the user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Formula: Centigrade = (Fahrenheit - 32) * 5/9
    centigrade = (fahrenheit - 32) * 5/9

    # Print the converted Centigrade value
    print("Temperature in Centigrade is:", centigrade)

    # Ask the user if they want to continue
    choice = input("Do you want to convert again? (yes/no): ")

    # If user types 'no', break the loop and end the program
    if choice.lower() != "yes":
        print("Thank you for using this converter!")
        break
