# Program to check NID Card eligibility

while True:
    # Taking age input from the user
    age = int(input("Enter your age: "))

    # Checking eligibility
    if age >= 18:
        print("✅ You are eligible to make an NID Card.")
    else:
        print("❌ You are NOT eligible to make an NID Card. Minimum age is 18.")

    # Asking user if they want to check again
    choice = input("\nDo you want to check again? (yes/no): ").lower()

    # If user types 'no', break the loop
    if choice == "no":
        print("Thanks for using this program!")
        break
