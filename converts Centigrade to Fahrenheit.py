# Program to convert Centigrade (Celsius) to Fahrenheit

while True:
    # Take temperature input in Centigrade from the user
    centigrade = float(input("Enter temperature in Centigrade: "))

    # Formula: Fahrenheit = (Centigrade * 9/5) + 32
    fahrenheit = (centigrade * 9/5) + 32

    # Print the converted Fahrenheit value
    print("Temperature in Fahrenheit is:", fahrenheit)

    # Ask the user if they want to continue
    choice = input("Do you want to convert again? (yes/no): ")

    # If user types 'no', break the loop and end the program
    if choice.lower() != "yes":
        print("Thank you for using this converter!")
        break
