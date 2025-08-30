# calculate the perimeter and area of a circle
# take radius as input
while True:
    radius = float(input("Enter the radius of the circle: "))
 
    # calculate perimeter (circumference)
    perimeter = 2 * 3.14 * radius

    # calculate area
    area = 3.14 * radius ** 2

    # print results
    print("Perimeter of the circle:", perimeter)
    print("Area of the circle:", area)
    # ask if the user wants to continue
    cont = input("Do you want to calculate again? (yes/no): ").lower()
    if cont != 'yes': #if user enters anything other than 'yes',
        print("Thank you for using the program. Goodbye!")
        break #exit the loop and end the program
    else:
        print("Let's calculate again!")