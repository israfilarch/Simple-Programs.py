# Python program to check if a year is a Leap Year

while True:
    # Take year input from the user
    year = int(input("Enter a year: "))

    # Check leap year condition:
    # Rule 1: If year is divisible by 400 → Leap Year
    # Rule 2: Else if divisible by 4 but not by 100 → Leap Year
    # Rule 3: Otherwise → Not a Leap Year
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year ")
    else:
        print(year, "is NOT a Leap Year ")

    # Ask user if they want to continue or exit
    choice = input("Do you want to check another year? (yes/no): ").lower()
    if choice != "yes":
        print("Program exited.")
        break
