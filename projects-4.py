# Start an infinite loop to repeatedly calculate the area
while True:
    # Take input from the user for the side length of the equilateral triangle
    side = float(input("Enter the side length of the equilateral triangle: "))

    # Use the formula for the area of an equilateral triangle: (√3 / 4) * side^2
    area = (3 ** 0.5 / 4) * (side ** 2)   # calculate the area

    # Display the calculated area
    print("The area of the equilateral triangle is:", area)

    # Ask the user if they want to calculate again, convert the response to lowercase
    again = input("Do you want to calculate again? (yes/no): ").lower()

    # If the user does not enter 'yes', exit the loop
    if again != 'yes':
        break
                  
