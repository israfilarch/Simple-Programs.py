# program to find the third angle of a triangle

while True:  
    # taking input from user
    angle1 = float(input("Enter the first angle of the triangle: "))   # first angle input
    angle2 = float(input("Enter the second angle of the triangle: "))  # second angle input

    # formula: third_angle = 180 - (angle1 + angle2)
    third_angle = 180 - (angle1 + angle2)   # calculate the third angle

    # printing the result
    print("The third angle of the triangle is:", third_angle)

    # ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ")  

    # if user says no, break the loop
    if choice.lower() != "yes":  
        print("Thanks for using this program!")  
        break
