def calculate_pay(hours, rate):
    # Calculate the total pay.
    total_pay = hours * rate

    # Return the total pay.
    return total_pay


# Ask the user for input.
hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly pay rate: "))

# Call the calculate_pay function and pass in the hours worked and hourly rate as arguments.
total_pay = calculate_pay(hours_worked, hourly_rate)

# Print the result.
print(f"The total pay is ${total_pay:.2f}")
