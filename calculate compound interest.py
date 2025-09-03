# Compound Interest Calculator Program

while True:
    # Take inputs from user
    P = float(input("Enter the Principal amount (P): "))   # Principal amount
    T = float(input("Enter the Time in years (T): "))      # Time in years
    R = float(input("Enter the Rate of Interest (R): "))   # Rate of Interest per year

    # Calculate the final amount using the formula: A = P * (1 + R/100) ** T
    A = P * (1 + R / 100) ** T

    # Calculate Compound Interest
    CI = A - P

    # Print the results
    print("The Compound Interest is:", CI)
    print("The Total Amount after", T, "years will be:", A)

    # Ask the user if they want to continue
    choice = input("Do you want to calculate again? (yes/no): ")

    # If user types 'no', stop the loop
    if choice.lower() == "no":
        print("Thank you for using the Compound Interest Calculator!")
        break
