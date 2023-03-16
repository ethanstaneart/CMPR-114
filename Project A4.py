# Declare global variables.
total = 0
average = 0


def get_numbers():
    # Get three numbers from the user.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Return the numbers as a tuple.
    return (num1, num2, num3)


def calculate_sum(num1, num2, num3):
    # Access the global variable.
    global total

    # Calculate the sum.
    total = num1 + num2 + num3


def calculate_average(num1, num2, num3):
    # Access the global variable.
    global average

    # Calculate the average.
    average = (num1 + num2 + num3) / 3


# Get the numbers from the user.
num1, num2, num3 = get_numbers()

# Calculate the sum and average.
calculate_sum(num1, num2, num3)
calculate_average(num1, num2, num3)

# Print the results.
print(f"The sum of {num1}, {num2}, and {num3} is {total}.")
print(f"The average of {num1}, {num2}, and {num3} is {average}.")
