# take the side length of the equilateral triangle as input
side = float(input("Enter the side length of the equilateral triangle: "))

# formula: (√3 / 4) * side^2
area = (3 ** 0.5 / 4) * (side ** 2)   # calculates the area using the formula

# print the result
print("The area of the equilateral triangle is:", area)