# Program to check whether a number is negative, positive, or zero

while True:
    # Taking input from the user
    num = float(input("Enter a number: "))

    # Checking conditions
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

    # Asking user if they want to continue
    choice = input("\nDo you want to check another number? (yes/no): ").lower()

    # If user types 'no', break the loop
    if choice == "no":
        print("Thanks for using this program!")
        break
