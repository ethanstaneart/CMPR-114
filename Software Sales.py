# Constants
PACKAGE_PRICE = 99

# Input from user
num_packages = int(input("Enter the number of packages purchased: "))

# Calculations
if num_packages < 10:
    discount = 0
elif num_packages < 20:
    discount = 0.1
elif num_packages < 50:
    discount = 0.2
elif num_packages < 100:
    discount = 0.3
else:
    discount = 0.4

total_price = num_packages * PACKAGE_PRICE
discount_amount = total_price * discount
final_price = total_price - discount_amount

# Output
if discount > 0:
    print("Discount amount:", discount_amount)
print("Total price after discount:", final_price)
