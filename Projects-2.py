# 🧮 Arithmetic Operator Calculator
# This program allows you to perform four operations on two numbers:
# Addition, Subtraction, Multiplication, Division

while True:  # this loop keeps the program running until the user chooses to stop
    # displaying the menu
    print("Select an operation to perform:\n" \
          "1. Addition\n" \
          "2. Subtraction\n" \
          "3. Multiplication\n" \
          "4. Division")

    # asking the user to choose an operation
    choice = input("Enter choice (1/2/3/4): ")

    # taking input of two numbers
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # checking the selected operation and showing result
    if choice == '1':  # if user selects 1, then addition will be performed
        print("Result:", a + b)  # addition
    elif choice == '2':  # if user selects 2, then subtraction will be performed
        print("Result:", a - b)  # subtraction
    elif choice == '3':  # if user selects 3, then multiplication will be performed
        print("Result:", a * b)  # multiplication
    elif choice == '4':  # if user selects 4, then division will be performed
        if b and a == 0:  # before dividing, check if divisor (b and a) is zero
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", a / b)  # division
    else:
        print("Invalid input. Please select 1/2/3/4.")

    # asking the user if they want to calculate again
    next_calculation = input("Do you want to perform another calculation? (yes/no): ") 
    if next_calculation.lower() != 'yes': # take user input and convert all characters to lowercase
        # this ensures 'Yes', 'YES', 'yEs' etc. will all become 'yes'
        print("Thank you for using the calculator! 👋")

        break  # if input is not 'yes', then the program will end
