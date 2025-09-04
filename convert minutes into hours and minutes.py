# Program to convert minutes (can be float) into hours, minutes and seconds

while True:
    # Take input in minutes (float to allow fractions)
    total_minutes = float(input("Enter total minutes: "))

    # Calculate hours (integer division)
    hours = int(total_minutes // 60)

    # Remaining minutes (take integer part)
    minutes = int(total_minutes % 60)

    # Calculate seconds from the decimal part of minutes
    seconds = round((total_minutes - int(total_minutes)) * 60)  # round used to avoid decimal errors (e.g., 29.999 → 30)

    # Print the result
    print(f"{hours} hour, {minutes} minute, and {seconds} second")

    # Ask user if they want to continue
    choice = input("Do you want to convert again? (yes/no): ")

    # Break the loop if the user does not want to continue
    if choice.lower() == "no":
        print("Thank you for using the Minutes Converter with Seconds!")
        break
