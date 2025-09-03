# Simple Interest Calculator Program

while True:
    # Take inputs from user
    P = float(input("Enter the Principal amount (P): "))   # Principal amount
    T = float(input("Enter the Time in years (T): "))      # Time in years
    R = float(input("Enter the Rate of Interest (R): "))   # Rate of Interest per year

    # Calculate Simple Interest using the formula: SI = (P * T * R) / 100
    SI = (P * T * R) / 100

    # Print the result
    print("The Simple Interest is:", SI)

    # Ask the user if they want to continue
    choice = input("Do you want to calculate again? (yes/no): ")

    # If user types 'no', stop the loop
    if choice.lower() == "no":
        print("Thank you for using the Simple Interest Calculator!")
        break
