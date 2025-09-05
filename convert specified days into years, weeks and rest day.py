# Program to convert given days into years, months, weeks and remaining days

while True:
    # Take input in days
    total_days = int(input("Enter total number of days: "))

    # Calculate years (365 days in a year)
    years = total_days // 365
    remaining_days = total_days % 365   # left after years

    # Calculate months (30 days in a month)
    months = remaining_days // 30
    remaining_days = remaining_days % 30   # left after months

    # Calculate weeks (7 days in a week)
    weeks = remaining_days // 7
    days = remaining_days % 7   # final leftover days

    # Print the result
    print(total_days, "days =", years, "year,", months, "month,", weeks, "week, and", days, "day")

    # Ask user if they want to continue
    choice = input("Do you want to convert again? (yes/no): ")

    # Break the loop if user chooses 'no'
    if choice.lower() == "no": #lower() method is used to convert the string to lowercase
        print("Thank you for using the Days Converter with Months!")
        break
