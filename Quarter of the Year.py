month = int(input("Enter a month as a number between 1 and 12: "))

if month < 1 or month > 12:
    print("Error: Invalid input. Month must be between 1 and 12.")
elif month <= 3:
    print("The month is in the first quarter.")
elif month <= 6:
    print("The month is in the second quarter.")
elif month <= 9:
    print("The month is in the third quarter.")
else:
    print("The month is in the fourth quarter.")
