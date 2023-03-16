def calculate_total_monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance):
    # Calculate the total monthly cost.
    total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance

    # Return the total monthly cost.
    return total_monthly_cost


# Ask the user for input.
loan_payment = float(input("Enter the monthly loan payment: "))
insurance = float(input("Enter the monthly insurance cost: "))
gas = float(input("Enter the monthly gas cost: "))
oil = float(input("Enter the monthly oil cost: "))
tires = float(input("Enter the monthly tire cost: "))
maintenance = float(input("Enter the monthly maintenance cost: "))

# Call the calculate_total_monthly_cost function and pass in the expenses as arguments.
total_monthly_cost = calculate_total_monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance)

# Calculate the total annual cost by multiplying the monthly cost by 12.
total_annual_cost = total_monthly_cost * 12

# Print the result.
print(f"The total monthly cost is ${total_monthly_cost:.2f}")
print(f"The total annual cost is ${total_annual_cost:.2f}")
