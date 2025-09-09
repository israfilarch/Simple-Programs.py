# Program to check whether a number is divisible by 5 or 11

while True:
    # Take input from user
    num = int(input("Enter a number: "))

    # Check divisibility
    if num % 5 == 0 and num % 11 == 0:
        print(num, "is divisible by both 5 and 11.")
    elif num % 5 == 0:
        print(num, "is divisible by 5.")
    elif num % 11 == 0:
        print(num, "is divisible by 11.")
    else:
        print(num, "is not divisible by 5 or 11.")

    # Ask user if they want to continue
    choice = input("Do you want to check another number? (yes/no): ")

    if choice.lower() == "no":
        print("Thank you for using the Divisibility Checker!")
        break
