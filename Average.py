MAX = 5  # The maximum number
total = 0.0  # Initialize an accumulator variable.

# Explain what we are doing.
print('This program calculates the sum and average of')
print(f'{MAX} numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total += number

# Calculate the average.
average = total / MAX

# Display the total and average of the numbers.
print(f'The total is {total}.')
print(f'The average is {average}.')
